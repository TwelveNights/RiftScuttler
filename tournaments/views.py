from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from common import utils
 
# Create your views here.
 
def index(request):
    tournament = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, year from tournaments")
        tournament = utils.dictfetchone(cursor)

    return render(request, "index.html", { "tournament": tournament })

def details(request, id, year):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.id, t.name
            FROM organizes o, series s, competes c
            JOIN teams t
            WHERE o.year=%s AND o.tournamentID = %s
            GROUP BY s.id
            ORDER BY s.id;
            """, [year, id])
        results = utils.dictfetchall(cursor)
    return HttpResponse(results)

def series(request, id, year, series):
    return HttpResponse("You made it to series!")

def match(request, id, year, series, number):
    return HttpResponse("You made it to match!")

