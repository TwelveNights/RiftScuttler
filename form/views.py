from django.shortcuts import render
from django.db import connection, transaction


# Create your views here.
# http://maxivak.com/executing-raw-sql-in-django/
# remove region attribute from teams
# remove functions to do with organizes


def insert_tournament_data(request, id, year, location, prize):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tournaments VALUES (%s %s %s %s)",
                   (id,
                    year,
                    location,
                    prize))
    transaction.commit()
    cursor.execute("SELECT * FROM tournaments", [])
    list_of_tournament = cursor.fetchall()
    context = {
        "object_list": list_of_tournament,
        "title": "Tournaments",
        "args": ("id", "year", "location", "prize"),
    }
    return render(request, "curator/tournaments.html", context)


def insert_series_data(id, bestOfCount):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO series VALUES (%s %s)",
                   (id,
                    bestOfCount))
    transaction.commit()


def insert_player_data(id, name, careerStartDate):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO players VALUES (%s %s %s)",
                   (id,
                    name,
                    careerStartDate))
    transaction.commit()


def insert_team_data(id, region, name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO teams VALUES (%s %s %s)",
                   (id,
                    region,
                    name))
    transaction.commit()


def insert_champion_data(name, category):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO champions VALUES (%s %s)",
                   (name,
                    category))
    transaction.commit()


def insert_item_data(id, name, basePrice):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items VALUES (%s %s)",
                   (id,
                    name,
                    basePrice))
    transaction.commit()


def insert_match_data(seriesID, matchNumber, date):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO matches VALUES (%s %s %s)",
                   (seriesID,
                    matchNumber,
                    date))
    transaction.commit()


def insert_bans_data(seriesID, matchNumber, name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO bans VALUES(%s %s %s)",
                   (seriesID,
                    matchNumber,
                    name))
    transaction.commit()


def insert_organizes_data(tournamentID, year, seriesID, stage):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO organizes VALUES (%s %s %s)",
                   (tournamentID,
                    year,
                    seriesID,
                    stage))
    transaction.commit()


def insert_competes_data(seriesID, team1ID, team1Region, team2ID, team2Region, winner):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO competes VALUES (%s %s %s %s %s %s)",
                   (seriesID,
                    team1ID,
                    team1Region,
                    team2ID,
                    team2Region,
                    winner))
    transaction.commit()


def insert_interacts_data(seriesID, matchNumber, playerID, itemID, time, isBuy, spent):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO competes VALUES (%s %s %s %s %s %s %s",
                   (seriesID,
                    matchNumber,
                    playerID,
                    itemID,
                    time,
                    isBuy,
                    spent))
    transaction.commit()


def insert_participates_data(tournamentID, teamID, teamRegion, year, stageReached):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO participates VALUES (%s %s %s %s %s)",
                   (tournamentID,
                    teamID,
                    teamRegion,
                    year,
                    stageReached))
    transaction.commit()


def insert_plays_data(seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced,
                      gold):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO plays VALUES (%s %s %s %s %s)",
                   (seriesID,
                    matchNumber,
                    playerID,
                    champion,
                    role,
                    kills,
                    deaths,
                    assists,
                    damageDealt,
                    wardsPlaced,
                    gold))
    transaction.commit()


def insert_registers_data(playerID, teamID, teamRegion, dateJoined, dateLeft):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO registers VALUES (%s %s %s %s %s)",
                   (playerID,
                    teamID,
                    teamRegion,
                    dateJoined,
                    dateLeft))
    transaction.commit()


def insert_scores_data(teamID, teamRegion, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons,
                       nexus):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scores VALUES (%s %s %s %s %s %s %s %s %s %s)",
                   (teamID,
                    teamRegion,
                    seriesID,
                    matchNumber,
                    inhibitors,
                    towers,
                    riftHeralds,
                    barons,
                    dragons,
                    nexus))
    transaction.commit()


def update_tournament_data(id, year, location, prize):
    cursor = connection.cursor()
    cursor.execute("UPDATE tournaments SET year=%s,location=%s,prize=%s WHERE id=%s AND year=%s", [year, location, prize, id])
    transaction.set_dirty()
    transaction.commit()


def update_series_data(id, bestOfCount):
    cursor = connection.cursor()
    cursor.execute("UPDATE series SET bestOfCount=%s WHERE id=%s", [id, bestOfCount])
    transaction.set_dirty()
    transaction.commit()


def update_player_data(id, name, careerStartDate):
    cursor = connection.cursor()
    cursor.execute("UPDATE players SET name=%s, careerStartDate=%s WHERE id=%s", [id, name, careerStartDate])
    transaction.set_dirty()
    transaction.commit()


def update_team_data(id, region, name):
    cursor = connection.cursor()
    cursor.execute("UPDATE teams SET region=%s, name=%s WHERE id=%s AND region=%s", [id, region, name])
    transaction.set_dirty()
    transaction.commit()


def update_champion_data(name, category):
    cursor = connection.cursor()
    cursor.execute("UPDATE champions SET region=%s, name=%s WHERE name=%s", [name, category])
    transaction.set_dirty()
    transaction.commit()


def update_item_data(id, region, name):
    cursor = connection.cursor()
    cursor.execute("UPDATE items SET region=%s, name=%s WHERE id=%s", [id, region, name])
    transaction.set_dirty()
    transaction.commit()


def update_match_data(seriesID, matchNumber, date):
    cursor = connection.cursor()
    cursor.execute("UPDATE matches SET seriesID=%s, matchNumber=%s, date=%s WHERE seriesID=%s AND matchNumber=%s", [seriesID, matchNumber, date])
    transaction.set_dirty()
    transaction.commit()


def update_bans_data(seriesID, matchNumber, name):
    cursor = connection.cursor()
    cursor.execute("UPDATE matches SET seriesID=%s, matchNumber=%s, date=%s WHERE seriesID=%s AND matchNumber=%s AND name=%s", [seriesID, matchNumber, name])
    transaction.set_dirty()
    transaction.commit()


def update_organizes_data(tournamentID, year, seriesID, stage):
    cursor = connection.cursor()
    cursor.execute("UPDATE organizes SET tournamentID=%s, seriesID=%s, stage=%s WHERE tournamentID=%s AND year=%s AND seriesID=%s", [tournamentID, year, seriesID, stage])
    transaction.set_dirty()
    transaction.commit()


def update_competes_data(seriesID, team1ID, team1Region, team2ID, team2Region, winner):
    cursor = connection.cursor()
    cursor.execute("UPDATE competes SET seriesID=%s, team1ID=%s, team1Region=%s, team2ID=%s, team2Region=%s, winner=%s WHERE seriesID=%s AND team1ID=%s AND team1Region=%s AND team2ID=%s AND team2Region=%s", [seriesID, team1ID, team1Region, team2ID, team2Region, winner])
    transaction.set_dirty()
    transaction.commit()


def update_interacts_data(seriesID, matchNumber, playerID, itemID, time, isBuy, spent):
    cursor = connection.cursor()
    cursor.execute("UPDATE interacts SET seriesID=%s, matchNumber=%s, playerID=%s, itemID=%s, time=%s, isBuy=%s, spent=%s WHERE seriesID=%s, matchNumber=%s, playerID=%s, itemID=%s, time=%s", [seriesID, matchNumber, playerID, itemID, time, isBuy, spent])
    transaction.set_dirty()
    transaction.commit()


def update_participates_data(tournamentID, teamID, teamRegion, year, stageReached):
    cursor = connection.cursor()
    cursor.execute("UPDATE participates SET tournamentID=%s, teamID=%s, teamRegion=%s, year=%s, stageReached=%s WHERE tournamentID=%s AND teamID=%s AND teamRegion=%s AND year=%s")
    transaction.set_dirty()
    transaction.commit()


def update_plays_data(seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced,
                      gold):
    cursor = connection.cursor()
    cursor.execute("UPDATE plays SET seriesID=%s, matchNumber=%s, playerID=%s, champion=%s, role=%s, kills=%s, deaths=%s, assists=%s, damageDealt=%s, wardsPlaced=%s WHERE seriesID=%s AND matchNumber=%s AND playerID=%s AND champion=%s", [seriesID, matchNumber, playerID, champion, role, kills, deaths, assists, damageDealt, wardsPlaced, gold])
    transaction.set_dirty()
    transaction.commit()


def update_registers_data(playerID, teamID, teamRegion, dateJoined, dateLeft):
    cursor = connection.cursor()
    cursor.execute("UPDATE registers SET playerID=%s, teamID=%s, teamRegion=%s, dateJoined=%s, dateLeft=%s WHERE playerID=%s AND teamID=%s AND teamRegion=%s", [playerID, teamID, teamRegion, dateJoined, dateLeft])
    transaction.set_dirty()
    transaction.commit()


def update_scores_data(teamID, teamRegion, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons,
                       nexus):
    cursor = connection.cursor()
    cursor.execute("UPDATE scores SET teamID=%s, teamRegion=%s, seriesID=%s, matchNumber=%s, inhibitors=%s, towers=%s, riftHeralds=%s, barons=%s, dragons=%s WHERE teamID=%s AND teamRegion=%s AND seriesID=%s AND matchNumber=%s",[teamID, teamRegion, seriesID, matchNumber, inhibitors, towers, riftHeralds, barons, dragons, nexus])
    transaction.set_dirty()
    transaction.commit()


def delete_tournament_data(id, year):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tournaments WHERE id=%s AND year=%s", [id, year])
    transaction.set_dirty()
    transaction.commit()


def delete_series_data(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM series WHERE id=%s", [id])
    transaction.set_dirty()
    transaction.commit()


def delete_player_data(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM players WHERE id=%s", [id])
    transaction.set_dirty()
    transaction.commit()


def delete_team_data(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM teams WHERE id=%s", [id])
    transaction.set_dirty()
    transaction.commit()


def delete_champion_data(name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM champions WHERE name=%s", [name])
    transaction.set_dirty()
    transaction.commit()


def delete_item_data(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM items WHERE id=%s", [id])
    transaction.set_dirty()
    transaction.commit()


def delete_match_data(seriesID, matchNumber):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM matches WHERE seriesID=%s AND matchNumber=%s", [seriesID, matchNumber])
    transaction.set_dirty()
    transaction.commit()


def delete_bans_data(seriesID, matchNumber):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bans WHERE seriesID=%s, matchNumber=%s", [seriesID, matchNumber])
    transaction.set_dirty()
    transaction.commit()


def delete_competes_data(seriesID, team1ID, team1Region, team2ID, team2Region):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM competes WHERE seriesID=%s, team1ID=%s, team1Region=%s, team2ID=%s, team2Region=%s", [seriesID, team1ID, team1Region, team2ID, team2Region])
    transaction.set_dirty()
    transaction.commit()


def delete_interacts_data(seriesID, matchNumber, playerID, itemID, time):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM interacts WHERE seriesID=%s, matchNumber=%s, playerID=%s, itemID=%s, time=%s", [seriesID, matchNumber, playerID, itemID, time])
    transaction.set_dirty()
    transaction.commit()


def delete_participates_data(tournamentID, teamID, teamRegion, year):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM participates WHERE tournamentID=%s, teamID=%s, teamRegion=%s, year=%s", [tournamentID, teamID, teamRegion, year])
    transaction.set_dirty()
    transaction.commit()


def delete_plays_data(seriesID, matchNumber, playerID, champion):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM plays WHERE seriesID=%s, matchNumber=%s, playerID=%s, champion=%s", [seriesID, matchNumber, playerID, champion])
    transaction.set_dirty()
    transaction.commit()


def delete_registers_data(playerID, teamID, teamRegion):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM registers WHERE playerID=%s, teamID=%s, teamRegion=%s", [playerID, teamID, teamRegion])
    transaction.set_dirty()
    transaction.commit()


def delete_scores_data(teamID, teamRegion, seriesID, matchNumber):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM scores WHERE teamID=%s, teamRegion=%s, seriesID=%s, matchNumber=%s", [teamID, teamRegion, seriesID, matchNumber])
    transaction.set_dirty()
    transaction.commit()

"""
def view_tournaments_data(request, id, year, location, prize):
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM tournaments", [id, year, location, prize])
    # row = cursor.fetchall()
    return render(request, "index.html", {})
"""


def view_tournaments_data(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tournaments", [])
    list_of_tournament = cursor.fetchall()
    context = {
        "object_list": list_of_tournament,
        "title": "Tournaments",
        "args": ("id", "year", "location", "prize")
    }
    return render(request, "curator/tournaments.html", context)


def form_home(request):
    if request.user.is_authenticated():
        context = {
            "title": "My User List",
            "args": range(0),
        }
    else:
        context = {
            "title": "List",
            "args": range(0),
        }
    return render(request, "curator/index.html", context)