from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.template import Context, Template
from .constant import *



def index(request):
    return HttpResponse("Hello, world. this will be the page show general play stat")

def detailView(request, pid):
    context = playdetail(pid)
    if context.get('error'):
        template = Template('{{ error }}')
        return HttpResponse(template.render(context))
    else:
        template = Template('the player show is {{ Id }}, Average Kill: {{ averageK }}, Average Death: {{ averageD }},'
                            'Average Assists: {{ averageA }},'
                            'Max Kill : {{ maxK }},'
                            'Max Death: {{ maxD }},'
                            'Max Assists: {{ maxA }},'
                            'Most Played Roles: {{ role }},'
                            'Ranking Points: {{ rank }} ')
        return HttpResponse(template.render(context))



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
            'support': BASE_POINT + SUPPORT_KDA_RATIO_WEIGHT*avgkdaRatio + SUPPORT_WARD_WEIGHT * wards,
            'adc': BASE_POINT + gold * ADC_GOLD_WEIGHT + ADC_KDA_WEIGHT * avgkdaRatio + ADC_MAX_KDA_WEIGHT * maxkdaRatio,
            'jungle': BASE_POINT + gold * JUNGLE_GOLD_WEIGHT + JUNGLE_AVG_KDA_WEIGHT * avgkdaRatio +
                      JUNGLE_MAX_KDA_WEIGHT * maxkdaRatio,
            'top': BASE_POINT + gold * TOP_GOLD_WEIGHT + TOP_AVG_KDA_WEIGHT * avgkdaRatio + TOP_MAX_KDA_WEIGHT * maxkdaRatio
                   + TOP_WARDS_WEIGHT * wards,
            'mid': BASE_POINT + MID_AVG_KDA_WEIGHT * avgkdaRatio + MID_MAX_KDA_WEIGHT * maxkdaRatio
    }.get(role)


# Create your views here.
