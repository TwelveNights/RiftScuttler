from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.template import Context, Template
from .constant import *
from django.shortcuts import render
from common import utils



def index(request):
    ranklist = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT name "
                       "FROM players ")
        player = cursor.fetchall()
        for item in player:
            context = dict({})
            playerDetail = playdetail(item[0])
            if 'rank' in playerDetail:
                context.update({'name': item[0]})
                context.update({'rank': playerDetail['rank']})
                context.update({'role': playerDetail['role']})
                ranklist.append(context)

    ranklist = sortRankList(ranklist)
    bestAdc = searchBestPlayer(ranklist,'adc')
    bestSupport = searchBestPlayer(ranklist, 'support')
    bestJungle = searchBestPlayer(ranklist, 'jungle')
    bestTop = searchBestPlayer(ranklist, 'top')
    bestMid = searchBestPlayer(ranklist, 'mid')
    contextlist = {'ranklist': ranklist,
                   'bestAdc': bestAdc,
                   'bestSupport': bestSupport,
                   'bestJungle': bestJungle,
                   'bestTop': bestTop,
                   'bestMid': bestMid}
    return render(request,'playerstatistics/index.html',contextlist)


def detailView(request, pname):
    context = playdetail(pname)
    return render(request,'playerstatistics/detail.html',context)



def playdetail(pname):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name "
                       "FROM players "
                       "WHERE name = %s", [pname])
        player = cursor.fetchall()
        cursor.execute("SELECT AVG(ps.kills) AS avgk, AVG(ps.deaths) AS avgd, AVG(ps.assists) AS avga "
                       "FROM players p, plays ps "
                       "WHERE p.name = %s AND p.name = ps.player ", [pname])
        avgkda = cursor.fetchall()
        cursor.execute("SELECT MAX(ps.kills) AS maxk, MAX(ps.deaths) AS maxd, MAX(ps.assists) AS maxa "
                       "FROM players p, plays ps "
                       "WHERE p.name = %s AND p.name = ps.player ", [pname])
        maxkda = cursor.fetchall()
        cursor.execute("SELECT player, role, MAX(rolecount), avgw, avgg, avgwd, avgcs, avgtJungle, avgeJungle, avgdmg "
                       "FROM roles "
                       "WHERE player = %s ", [pname])
        role = utils.dictfetchall(cursor)

        cursor.execute("SELECT DISTINCT seriesID "
                       "FROM plays "
                       "WHERE player = %s", [pname])
        series = utils.dictfetchall(cursor)

        cursor.execute("SELECT teamID "
                       "FROM players p, registers r "
                       "WHERE r.player =  p.name AND p.name = %s ", [pname])
        team = cursor.fetchone()



        if not player:
            return Context({'error': 'There is no such player with SummonerName: %s' % pname})
        elif role[0]['role'] is None:
            return Context({'error': 'The player: %s, has not played any game before' % pname})
        else:
            rank = calcranking(avgkda[0][0], avgkda[0][1], avgkda[0][2],
                               maxkda[0][0], maxkda[0][1], maxkda[0][2],
                               role[0]['role'], role[0]['avgw'], role[0]['avgg'], role[0]['avgwd'], role[0]['avgcs'],
                               role[0]['avgtJungle'], role[0]['avgeJungle'], role[0]['avgdmg'])
            context = {
                'name': pname,
                'averageK': avgkda[0][0],
                'averageD': avgkda[0][1],
                'averageA': avgkda[0][2],
                'maxK': maxkda[0][0],
                'maxD': maxkda[0][1],
                'maxA': maxkda[0][2],
                'role': role[0]['role'],
                'avgw': role[0]['avgw'],
                'avgg': role[0]['avgg'],
                'avgwd': role[0]['avgwd'],
                'avgcs': role[0]['avgcs'],
                'avgtJungle': role[0]['avgtJungle'],
                'avgeJungle': role[0]['avgeJungle'],
                'avgdmg': role[0]['avgdmg'],
                'rank': rank,
                'team': team[0],
                'series': series}
            return Context(context)



def calcranking(avgk, avgd, avga, maxk, maxd, maxa, role, wards, gold, wardskill, cs, teamjungle, enemeyjungle, dmg):
    avgkdaRatio = (avga + avgk) / (avga + avgd + avgk)
    maxkdaRatio = (maxa + maxk) / (maxa + maxd + maxk)
    return {
            'support': int(BASE_POINT + SUPPORT_KDA_RATIO_WEIGHT*avgkdaRatio + SUPPORT_WARD_WEIGHT * wards +
                           SUPPORT_WADR_KILL_WEIGHT*wardskill),
            'adc': int(BASE_POINT + gold * ADC_GOLD_WEIGHT + ADC_KDA_WEIGHT * avgkdaRatio + ADC_MAX_KDA_WEIGHT * maxkdaRatio +
                       ADC_DAMAGE_WEIGHT *dmg + ADC_CS_WEIGHT*cs),
            'jungle': int(BASE_POINT + gold * JUNGLE_GOLD_WEIGHT + JUNGLE_AVG_KDA_WEIGHT * avgkdaRatio +
                      JUNGLE_MAX_KDA_WEIGHT * maxkdaRatio + JUNGLE_ENEMY_WEIGHT*enemeyjungle + JUNGLE_TEAM_WEIGHT*teamjungle),
            'top': int(BASE_POINT + gold * TOP_GOLD_WEIGHT + TOP_AVG_KDA_WEIGHT * avgkdaRatio + TOP_MAX_KDA_WEIGHT * maxkdaRatio
                   + TOP_WARDS_WEIGHT * wards),
            'mid': int(BASE_POINT + MID_AVG_KDA_WEIGHT * avgkdaRatio + MID_MAX_KDA_WEIGHT * maxkdaRatio + MID_DMG_WEIGHT*dmg)
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


def searchBestPlayer(ranklist, role):
    for x in ranklist:
        if x['role'] == role:
            return {'name': x['name']}
    return 'N/A'

# Create your views here.
