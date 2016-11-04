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
        cursor.execute("DROP VIEW IF EXISTS roles;")
        cursor.execute("CREATE VIEW IF NOT EXISTS roles AS "
                        "SELECT "
                        "playerID, "
                        "role, "
                        "COUNT(*) AS rolecount, "
                        "AVG(wardsPlaced) AS  avgw, "
                        "AVG(gold) AS avgg "
                        "FROM plays  "
                        "GROUP BY playerID, role ")
        cursor.execute("SELECT playerID, role, MAX(rolecount), avgw, avgg "
                       "FROM roles "
                       "WHERE playerID = %s ", [pid])
        role = cursor.fetchall()
        rank = calcranking(avgkda[0][0], avgkda[0][1], avgkda[0][2],
                           maxkda[0][0], maxkda[0][1], maxkda[0][2],
                           role[0][1], role[0][3], role[0][4])
        if not player:
            html = "<html><body> Player with pid <b>%s</b> does not exists</body></html>" % pid
        else:
            html = "<html><body><p>the player showing now is <b>%s</b>." \
                   "</p> <p>averageK/D/A:  %s/%s/%s </p>" \
                   "<p>maxK/D/A: %s/%s/%s </p>" \
                   "<p>most role played: %s </p>" \
                   "<p>rankPoint with the most played role: %s</body></html>"\
                   % (player[0][0], avgkda[0][0], avgkda[0][1], avgkda[0][2],
                      maxkda[0][0], maxkda[0][1], maxkda[0][2], role[0][1], rank)
        return HttpResponse(html)



def calcranking(avgk, avgd, avga, maxk, maxd, maxa, role, wards, gold):
    if avgk is None \
            or avgd is None \
            or avga is None \
            or maxk is None \
            or maxd is None \
            or maxa is None \
            or role is None \
            or wards is None \
            or gold is None:
        return 'there is invalid data with this player, thus giving base point: 1000'
    else:
        return {
            'support': 1000 + 200 * ((avga + avgk) / (avga + avgd + avgk)) + 100 * wards / 3,
            'adc': 1000 + gold / 100 + 800 * ((avga + avgk) / (avga + avgd + avgk)) + 200 * (
            (maxa + maxk) / (maxa + maxd + maxk)),
            'jungle': 1000 + gold / 150 + 1000 * ((avga + avgk) / (avga + avgd + avgk)) + 300 * (
            (maxa + maxk) / (maxa + maxd + maxk)),
            'top': 1000 + gold / 150 + 800 * ((avga + avgk) / (avga + avgd + avgk)) + 200 * (
            (maxa + maxk) / (maxa + maxd + maxk)) + 100 * wards / 6,
            'mid': 1000 + 1000 * ((avga + avgk) / (avga + avgd + avgk)) + 500 * ((maxa + maxk) / (maxa + maxd + maxk))
        }.get(role, 1000)


# Create your views here.
