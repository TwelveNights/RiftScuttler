from django.shortcuts import render
from django.db import connection
from django.template import Context, Template
from django.shortcuts import render
from common import utils

# Create your views here.


def index(request):
    championlist = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, id "
                       "FROM champions ")
        champions = utils.dictfetchall(cursor)
        for item in champions:
            context = dict({})
            context.update({'name': item['name']})
            context.update({'id': item['id']})
            if 'Dr.' in item['name']:
                urlname = (item['name']).replace(".", "").replace(" ", "")
                context.update({'urlname': urlname})
            elif 'Fiddle' in item['name']:
                context.update({'urlname': 'FiddleSticks'})
            elif 'Jarvan' in item['name']:
                context.update({'urlname': 'JarvanIV'})
            elif 'Wukong' in item['name']:
                context.update({'urlname': 'MonkeyKing'})
            elif "Kog'Maw" in item['name']:
                context.update({'urlname': 'KogMaw'})
            elif "Rek'Sai" in item['name']:
                context.update({'urlname': 'RekSai'})
            else:
                context.update({'urlname': ((item['name'].lower().replace("'", "")).title()).replace(" ", "")})
            championlist.append(context)
    contextlist = {'championlist': championlist}
    return render(request,'champions/index.html', contextlist)


def detailView(request, cid):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT c.name "
            "FROM champions c "
            "WHERE NOT EXISTS "
            " (SELECT DISTINCT t.year, t.name "
            "  FROM tournaments t"
            "  EXCEPT "
            "  SELECT DISTINCT t.year, t.name"
            "  FROM plays ps, registers r, participates pt, tournaments t"
            "  WHERE c.id = ps.championID AND ps.player = r.player AND r.teamID = pt.teamID AND pt.tournamentID = t.id AND c.id = %s ) ", [cid])
        parti = cursor.fetchone()
        context.update({'parti': bool(parti)})
        cursor.execute(
            "SELECT c.name "
            "FROM champions c "
            "WHERE c.id = %s", [cid])
        name = utils.dictfetchone(cursor)
        context.update({'name': name['name']})
        urlname = name['name'].replace(" ", "").replace("'", "").replace(".", "").lower()
        context.update({'urlname': urlname})
        cursor.execute(
            "SELECT ps2.player, COUNT(*) "
            "FROM plays ps2 "
            "WHERE ps2.championID  = %s "
            "GROUP BY ps2.player "
            "HAVING COUNT(*) >= "
            " ("
            "  SELECT MAX(playcount) "
            "  FROM "
            "   (SELECT ps1.player, COUNT(ps1.championID) as playcount "
            "    FROM plays ps1 "
            "    WHERE ps1.championID = ps2.championID "
            "    GROUP BY ps1.player)) ",[cid]
        )
        bestplayertable = cursor.fetchall()
        bestplayer = []
        if bestplayertable:
            for item in bestplayertable:
                bestplayer.append(item[0])
        context.update({'bestplayer': bestplayer})
    return render(request, 'champions/detail.html', context)
