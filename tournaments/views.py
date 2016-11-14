from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, Http404
from common import utils

# Create your views here.

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from tournaments")
        tournaments = utils.dictfetchall(cursor)

    return render(request, "tournaments/index.html", {"tournaments": tournaments})


def detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT c.seriesID AS series, c.teamID AS team, c.blueSide AS blueSide "
                       "FROM competes c "
                       "WHERE c.seriesID in ("
                       "SELECT seriesID FROM organizes WHERE tournamentID = %s) "
                       "ORDER BY c.seriesID", [id])
        results = utils.dictfetchall(cursor)

        if not results:
            raise Http404("There are no games with id '{0}'".format(id))

    all_series = {}

    for result in results:
        series = result["series"]
        team = result["team"]
        blue = result["blueSide"]

        if series not in all_series:
            all_series[series] = {}

        with connection.cursor() as cursor:
            cursor.execute("SELECT s.seriesID series, s.teamID team, SUM(s.nexus) score "
                           "FROM scores s JOIN matches m ON "
                           "(s.seriesID = m.seriesID AND s.matchNumber = m.matchNumber) "
                           "WHERE m.seriesID = %s AND s.teamID = %s"
                           "GROUP BY s.seriesID, s.teamID", [series, team])
            score = utils.dictfetchone(cursor)

        all_series[series]["blue" if blue == 1 else "purple"] = {
            "team": team,
            "score": score["score"]
        }

    with connection.cursor() as cursor:
        tournament = utils.dictfetchone(
            cursor.execute("SELECT name, year FROM tournaments WHERE id = %s", [id]))

    return render(request, "tournaments/detail.html",
                  {"data": all_series, "tournament": tournament})
