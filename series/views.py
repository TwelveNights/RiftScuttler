from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, Http404
from common import utils
from . import helpers

def detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, bestOfCount FROM series WHERE id = %s", [id])
        series = utils.dictfetchone(cursor)
        series["matches"] = []

        cursor.execute("SELECT teamID, blueSide "
                       "FROM competes "
                       "WHERE seriesID = %s", [id])

        for result in utils.dictfetchall(cursor):
            series["blue" if result["blueSide"] == 1 else "purple"] = {
                "team": result["teamID"],
                "members": []}

        cursor.execute("SELECT seriesID, matchNumber, date(matchDate) matchDate "
                       "FROM matches WHERE seriesID = %s ORDER BY matchNumber", [id])

        matches = utils.dictfetchall(cursor)
        first_match = matches[0]

        cursor.execute("SELECT summonerName FROM plays WHERE seriesID = %s AND matchNumber = %s",
                       [id, first_match["matchNumber"]])

        for result in utils.dictfetchall(cursor):
            name = result["summonerName"]
            team = helpers.find_team(name, first_match["matchDate"])

            series["blue" if team == series["blue"]["team"] else "purple"]["members"].append(name)

        for match in matches:

            match_number = match["matchNumber"]
            match_details = {"blue": {
                "kills": 0,
                "deaths": 0,
                "assists": 0
            }, "purple": {
                "kills": 0,
                "deaths": 0,
                "assists": 0
            }, "number": match_number}
            cursor.execute("SELECT c.name name, b.pickTurn "
                           "FROM champions c, bans b "
                           "WHERE b.seriesID = %s AND b.matchNumber = %s AND b.championID = c.id "
                           "ORDER BY b.pickTurn", [id, match_number])

            match_details["bans"] = [result["name"] for result in utils.dictfetchall(cursor)]

            for color in ["blue", "purple"]:
                for member in series[color]["members"]:
                    cursor.execute("SELECT p.kills kills, p.deaths deaths, p.assists assists "
                                   "FROM plays p WHERE p.seriesID = %s "
                                   "AND p.matchNumber = %s AND p.summonerName = %s",
                                   [match["seriesID"], match_number, member])

                    result = utils.dictfetchone(cursor)
                    match_details[color]["kills"] += result["kills"]
                    match_details[color]["deaths"] += result["deaths"]
                    match_details[color]["assists"] += result["assists"]
            series["matches"].append(match_details)

    return render(request, "series/detail.html", {"data": series})
