from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse, Http404
from django.urls import reverse
from common import utils
from . import helpers

def detail(request, id, stat=None):
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

        cursor.execute("SELECT player FROM plays WHERE seriesID = %s AND matchNumber = %s",
                       [id, first_match["matchNumber"]])

        for result in utils.dictfetchall(cursor):
            name = result["player"]
            team = helpers.find_team(name, first_match["matchDate"])

            series["blue" if team == series["blue"]["team"] else "purple"]["members"].append(name)

        for match in matches:
            match_number = match["matchNumber"]
            match_details = {"blue": {}, "purple": {}}
            cursor.execute("SELECT c.name name, b.pickTurn "
                           "FROM champions c, bans b "
                           "WHERE b.seriesID = %s AND b.matchNumber = %s AND b.championID = c.id "
                           "ORDER BY b.pickTurn", [id, match_number])

            match_details["bans"] = [result["name"] for result in utils.dictfetchall(cursor)]
            values = ["kills", "deaths", "assists"]
            if stat in helpers.STATISTICS:
                values = [stat]
            elif stat is not None:
                return redirect(reverse('series:detail', args=[id]), permanent=True)
            series["stats"] = values

            for color in ["blue", "purple"]:
                for member in series[color]["members"]:
                    sql = ""

                    for i, value in enumerate(values):
                        if i == 0:
                            sql += "p.{0} {0}".format(value)
                        else:
                            sql += ", p.{0} {0}".format(value)

                    cursor.execute("SELECT " + sql + ", c.name champion "
                                   "FROM plays p, champions c WHERE p.seriesID = %s "
                                   "AND p.matchNumber = %s AND p.player = %s AND c.id = p.championID",
                                   [match["seriesID"], match_number, member])

                    result = utils.dictfetchone(cursor)
                    match_details[color][member] = {"champion": result["champion"]}
                    if len(values) == 1:
                        match_details[color][member]['stat'] = result[value]
                    else:
                        for value in values:
                            match_details[color][member][value] = result[value]

            series["matches"].append(match_details)
    series["available_stats"] = helpers.STATISTICS
    return render(request, "series/detail.html", {"data": series})
