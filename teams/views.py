from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, Http404
from common import utils

# Create your views here.

def detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.name, t.id "
                       "FROM teams t, registers r, players p "
                       "WHERE t.id = %s AND t.id = r.teamID AND r.player = p.name", [id])
        results = utils.dictfetchall(cursor)

        cursor.execute("SELECT wins FROM wins WHERE teamID = %s", [id])
        wins = utils.dictfetchone(cursor)["wins"]

    return render(request, "teams/detail.html", {"data": results, "wins": wins})

def index(request, region=None):
    with connection.cursor() as cursor:
        if region is None:
            cursor.execute("SELECT * FROM teams")
        else:
            cursor.execute("SELECT * FROM teams WHERE region = %s", [region])

        results = utils.dictfetchall(cursor)

        cursor.execute("SELECT DISTINCT region FROM teams")

        regions = [r["region"] for r in utils.dictfetchall(cursor)]

    return render(request, "teams/index.html", {"data": results, "regions": regions})
