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
        player = cursor.fetchall()
        cursor.execute("SELECT AVG(ps.kills) AS avgk, AVG(ps.deaths) AS avgd, AVG(ps.assists) AS avga "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        avgkda = cursor.fetchall()

        cursor.execute("SELECT MAX(ps.kills) AS maxk, MAX(ps.deaths) AS maxd, MAX(ps.assists) AS maxa "
                       "FROM players p, plays ps "
                       "WHERE p.id = %s AND p.id = ps.playerID ", [pid])
        maxkda = cursor.fetchall()
        cursor.execute("DROP VIEW roleplaycount")
        cursor.execute("CREATE VIEW roleplaycount AS "
                       "SELECT ps.role,p.id ,COUNT(ps.role) AS rolecount "
                       "FROM players p, plays ps "
                       "WHERE p.id = ps.playerID "
                       "GROUP BY ps.role ")
        cursor.execute("SELECT r1.role "
                       "FROM roleplaycount r1 "
                       "WHERE r1.id = %s AND r1.rolecount >= "
                       " (SELECT MAX(rolecount)"
                       "  FROM roleplaycount r2"
                       "  WHERE r2.id = %s)", [pid, pid])
        role = cursor.fetchall()
        rank = calcranking(0,0,0,0,0,0)
        html = "<html><body><p>the player showing now is <b>%s</b>." \
               "</p> <p>averageK/D/A:  %s/%s/%s </p>" \
               "<p>maxK/D/A: %s/%s/%s </p>" \
               "<p>most role played: %s </p>" \
               "<p>rankPoint with the most played role: %s</body></html>"\
               % (player[0][0], avgkda[0][0], avgkda[0][1], avgkda[0][2], maxkda[0][0], maxkda[0][1], maxkda[0][2], role, rank)
        return HttpResponse(html)



def calcranking(avgk,avgd,avga,maxk,maxd,maxa):
    return 1000


# Create your views here.
