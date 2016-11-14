from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, Http404
from common import utils

# Create your views here.

def detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.name, t.id "
                       "FROM teams t, registers r, players p "
                       "WHERE t.id = %s AND t.id = r.teamID AND r.summonerName = p.name", [id])
        results = utils.dictfetchall(cursor)

    return render(request, "teams/detail.html", {"data": results})

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM teams")
        results = utils.dictfetchall(cursor)
    return render(request, "teams/index.html", {"data": results})
