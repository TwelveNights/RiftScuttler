from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, Http404
from common import utils

def series(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT s.id id, s.bestOfCount bestOf, m.date date, m.matchNumber number "
                       "FROM series s, matches m "
                       "WHERE s.id = %s AND s.id = m.seriesID", [id])
        results = utils.dictfetchall(cursor)

    return render(request, "series/series.html", {"data": results})

def match(request, id, number):
    pass