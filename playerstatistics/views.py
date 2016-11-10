from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.template import Context, Template
from .constant import *
from django.shortcuts import render



def index(request):
    ranklist = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name "
                       "FROM players ")
        player = cursor.fetchall()
        for item in player:
            context = dict({})
            playerDetail = playdetail(item[0])
            if 'rank' in playerDetail:
                context.update({'Id': item[0]})
                context.update({'name': item[1]})
                context.update({'rank': playerDetail['rank']})
                ranklist.append(context)
    ranklist = sortRankList(ranklist);
    contextlist = {'ranklist': ranklist}
    return render(request,'index.html',contextlist)

def detailView(request, pid):
    context = playdetail(pid)
    return render(request,'detail.html',context)



def playdetail(pid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name "
                       "FROM players "
                       "WHERE id = %s", [pid])
        player = cursor.fetchall()
        cursor.execute("SELECT AVG(ps.kills) AS avgk, AVG(ps.deaths) AS avgd, AVG(ps.assists) AS avga "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        avgkda = cursor.fetchall()
        cursor.execute("SELECT MAX(ps.kills) AS maxk, MAX(ps.deaths) AS maxd, MAX(ps.assists) AS maxa "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        maxkda = cursor.fetchall()
        cursor.execute("SELECT playerID, role, MAX(rolecount), avgw, avgg "
                       "FROM roles "
                       "WHERE playerID = %s ", [pid])
        role = cursor.fetchall()

        if not player:
            return Context({'error': 'There is no such player with playerID: %s' % pid})
        elif role[0][1] is None:
            return Context({'error': 'The player: %s, has not played any game before' % player[0][0]})
        else:
            rank = calcranking(avgkda[0][0], avgkda[0][1], avgkda[0][2],
                               maxkda[0][0], maxkda[0][1], maxkda[0][2],
                               role[0][1], role[0][3], role[0][4])
            context = {
                'Id': player[0][0],
                'averageK': avgkda[0][0],
                'averageD': avgkda[0][1],
                'averageA': avgkda[0][2],
                'maxK': maxkda[0][0],
                'maxD': maxkda[0][1],
                'maxA': maxkda[0][2],
                'role': role[0][1],
                'rank': rank}
            return Context(context)



def calcranking(avgk, avgd, avga, maxk, maxd, maxa, role, wards, gold):
    avgkdaRatio = (avga + avgk) / (avga + avgd + avgk)
    maxkdaRatio = (maxa + maxk) / (maxa + maxd + maxk)
    return {
            'support': int(BASE_POINT + SUPPORT_KDA_RATIO_WEIGHT*avgkdaRatio + SUPPORT_WARD_WEIGHT * wards),
            'adc': int(BASE_POINT + gold * ADC_GOLD_WEIGHT + ADC_KDA_WEIGHT * avgkdaRatio + ADC_MAX_KDA_WEIGHT * maxkdaRatio),
            'jungle': int(BASE_POINT + gold * JUNGLE_GOLD_WEIGHT + JUNGLE_AVG_KDA_WEIGHT * avgkdaRatio +
                      JUNGLE_MAX_KDA_WEIGHT * maxkdaRatio),
            'top': int(BASE_POINT + gold * TOP_GOLD_WEIGHT + TOP_AVG_KDA_WEIGHT * avgkdaRatio + TOP_MAX_KDA_WEIGHT * maxkdaRatio
                   + TOP_WARDS_WEIGHT * wards),
            'mid': int(BASE_POINT + MID_AVG_KDA_WEIGHT * avgkdaRatio + MID_MAX_KDA_WEIGHT * maxkdaRatio)
    }.get(role)


def sortRankList(ranklist):
    less = []
    equal = []
    greater = []
    if len(ranklist) > 1:
        pivot = ranklist[0]['rank']
        for x in ranklist:
            if x['rank'] < pivot:
                less.append(x)
            if x['rank'] == pivot:
                equal.append(x)
            if x['rank'] > pivot:
                greater.append(x)
        return sortRankList(greater)+equal+sortRankList(less)
    else:
        return ranklist
# Create your views here.
