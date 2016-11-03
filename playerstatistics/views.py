from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection



def index(request):
    return HttpResponse("Hello, world. this will be the page show general play stat")



def playdetail(request, pid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name "
                       "FROM players "
                       "WHERE id = %s", [pid])
        player = cursor.fetchone()
        cursor.execute("SELECT AVG(ps.kills) AS avgk, AVG(ps.deaths) AS avgd, AVG(ps.assists) AS avga "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        avgkda = cursor.fetchall()

        cursor.execute("SELECT MAX(ps.kills) AS avgk, MAX(ps.deaths) AS avgd, MAX(ps.assists) AS avga "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        maxkda = cursor.fetchall()
        rank = calcranking(0,0,0,0,0,0)
        html = "<html><body><p>the player showing now is <b>%s</b>.</p> <p>averageKDA:  </p></body></html>" % player
        return HttpResponse(html)



def calcranking(avgk,avgd,avga,maxk,maxd,maxa):
    return 1000


# Create your views here.
