from .tables import *
from django.db import transaction

# Helper functions:


def insert_data(cursor, table):
    sql = "INSERT INTO " + table.tname + " VALUES ("
    length_args = len(table.args)
    for i, args in enumerate(table.args):
        if isinstance(args, str):
            sql += "\'" + args + "\'"
        else:
            sql += "\'" + str(args) + "\'"
        if i == (length_args - 1):
            break
        sql += ", "
    sql += ")"
    print(sql)
    cursor.execute(sql, [])
    transaction.commit()


def delete_data(cursor, table):
    sql = "DELETE FROM " + table.tname + " WHERE "
    pk_length = len(table.pk)
    for i, pk in enumerate(table.pk):
        sql += pk[0] + "="
        if isinstance(table.args[i], str):
            sql += "\'" + table.args[i] + "\'"
        else:
            sql += "\'" + str(table.args[i]) + "\'"
        if i == (pk_length - 1):
            break
        sql += " AND "
    cursor.execute(sql, [])
    transaction.commit()


def edit_data(cursor, table):
    sql = "UPDATE " + table.tname + " SET "
    pk_length = len(table.pk)
    non_pk_length = len(table.non_pk)
    for j, col in enumerate(table.non_pk):
        if isinstance(table.non_pk_args[j], str):
            sql += col + "=" + "\'" + table.non_pk_args[j] + "\'"
        else:
            sql += col + "=" + "\'" + str(table.non_pk_args[j]) + "\'"
        if j < (non_pk_length - 1):
            sql += ", "
    sql += " WHERE "
    for i, pk in enumerate(table.pk):
        sql += pk[0] + "="
        if isinstance(table.args[i], str):
            sql += "\'" + table.args[i] + "\'"
        else:
            sql += "\'" + str(table.args[i]) + "\'"
        if i == (pk_length - 1):
            break
        sql += " AND "
    cursor.execute(sql, [])
    transaction.commit()


def select_data(cursor, tname):
    sql = "SELECT * FROM "
    sql += tname
    cursor.execute(sql, [])
    list_of_data = cursor.fetchall()
    return list_of_data


def reorder_dictionary(table):
    new_table_args = []
    for i, cols in enumerate(table.cols):
        for j, args in enumerate(table.args):
            if cols[0] == args[0]:
                new_table_args.append(args[1])
                break
    return new_table_args


def get_args(column_list):
    args = []
    for cols in column_list:
        args.append(cols[0])
    return args


def create_context(tname, form, list_of_data, args):
    value = tname.title()
    context = {
        "form": form,
        "object_list": list_of_data,
        "title": value,
        "args": args,
    }
    return context


def get_non_pk_args(table):
    args = []
    pk_length = len(table.pk)
    for i, cols in enumerate(table.cols):
        if i >= pk_length:
            args.append(table.args[i])
    return args


def reset_table(table):
    for attr, value in table.__dict__.items():
        if isinstance(attr, str):
            value[0] = ""
        elif isinstance(attr, list):
            value[0] = []


def check_page_and_return_table(request):
    abs_url = request.get_full_path()
    table = StructData()
    if abs_url.find("_tournaments/") != -1:
        table.tname = "tournaments"
        table.cols = [("id", "charfield"), ("year", "int"), ("location", "charfield"), ("prize", "int")]
        table.args = []
        table.pk = [("id", "charfield"), ("year", "int")]
        table.non_pk = ["location", "prize"]
        table.non_pk_args = []
    elif abs_url.find("_series/") != -1:
        table.tname = "series"
        table.cols = [("id", "int"), ("bestOfCount", "int")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = ["bestOfCount"]
        table.non_pk_args = []
    elif abs_url.find("_champions/") != -1:
        table.tname = "champions"
        table.cols = [("name", "charfield"), ("category", "charfield")]
        table.args = []
        table.pk = [("name", "charfield")]
        table.non_pk = ["category"]
        table.non_pk_args = []
    elif abs_url.find("_items/") != -1:
        table.tname = "items"
        table.cols = [("id", "int"), ("name", "charfield"), ("basePrice", "int")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = ["name", "basePrice"]
        table.non_pk_args = []
    elif abs_url.find("_players/") != -1:
        table.tname = "players"
        table.cols = [("id", "int"), ("name", "charfield"), ("careerStartDate", "datetime")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = ["name", "careerStartDate"]
        table.non_pk_args = []
    elif abs_url.find("_teams/") != -1:
        table.tname = "teams"
        table.cols = [("id", "charfield"), ("region", "charfield"), ("name", "charfield")]
        table.args = []
        table.pk = [("id", "charfield"), ("region", "charfield")]
        table.non_pk = ["name"]
        table.non_pk_args = []
    elif abs_url.find("_matches/") != -1:
        table.tname = "matches"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("date", "datetime")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int")]
        table.non_pk = ["date"]
        table.non_pk_args = []
    elif abs_url.find("_bans/") != -1:
        table.tname = "bans"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("name", "charfield")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("name", "charfield")]
        table.non_pk = []
        table.non_pk_args = []
    elif abs_url.find("_organizes/") != -1:
        table.tname = "organizes"
        table.cols = [("tournamentID", "charfield"), ("year", "int"), ("seriesID", "int"), ("stage", "charfield")]
        table.args = []
        table.pk = [("tournamentID", "int"), ("year", "int"), ("seriesID", "int")]
        table.non_pk = ["stage"]
        table.non_pk_args = []
    elif abs_url.find("_competes/") != -1:
        table.tname = "competes"
        table.cols = [("seriesID", "int"), ("team1ID", "charfield"), ("team1Region", "charfield"), ("team2ID", "charfield"), ("team2Region", "charfield"), ("winner", "charfield")]
        table.args = []
        table.pk = [("seriesID", "int"), ("team1ID", "charfield"), ("team1Region", "charfield"), ("team2ID", "charfield"), ("team2Region", "charfield")]
        table.non_pk = ["winner"]
        table.non_pk_args = []
    elif abs_url.find("_interacts/") != -1:
        table.tname = "interacts"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("itemID", "int"), ("time", "int"), ("isBuy", "boolean"), ("spent", "int")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("itemID", "int"), ("time", "int")]
        table.non_pk = ["isBuy", "spent"]
        table.non_pk_args = []
    elif abs_url.find("_participates/") != -1:
        table.tname = "participates"
        table.cols = [("tournamentID", "charfield"), ("teamID", "charfield"), ("teamRegion", "charfield"), ("year", "int"), ("stageReached", "charfield")]
        table.args = []
        table.pk = [("tournamentID", "int"), ("teamID", "charfield"), ("teamRegion", "charfield"), ("year", "int")]
        table.non_pk = ["stage"]
        table.non_pk_args = ["stageReached"]
    elif abs_url.find("_plays/") != -1:
        table.tname = "plays"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("champion", "charfield"), ("role", "charfield"), ("kills", "int"), ("deaths", "int"), ("assists", "int"), ("damageDealt", "int"), ("wardsPlaced", "int"), ("gold", "int")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("champion", "charfield")]
        table.non_pk = ["role", "kills", "deaths", "assists", "damageDealt", "wardsPlaced", "gold"]
        table.non_pk_args = []
    elif abs_url.find("_registers/") != -1:
        table.tname = "registers"
        table.cols = [("playerID", "int"), ("teamID", "charfield"), ("teamRegion", "charfield"), ("dateJoined", "date"), ("dateLeft", "date")]
        table.args = []
        table.pk = [("playerID", "int"), ("teamID", "charfield"), ("teamRegion", "charfield")]
        table.non_pk = ["dateJoined", "dateLeft"]
        table.non_pk_args = []
    elif abs_url.find("_scores/") != -1:
        table.tname = "scores"
        table.cols = [("teamID", "charfield"), ("teamRegion", "charfield"), ("seriesID", "int"), ("matchNumber", "int"), ("inhibitors", "int"), ("towers", "int"), ("riftHeralds", "int"), ("barons", "int"), ("dragons", "int"), ("nexus", "int")]
        table.args = []
        table.pk = [("teamID", "charfield"), ("teamRegion", "charfield"), ("seriesID", "int"), ("matchNumber", "int")]
        table.non_pk = ["inhibitors", "towers", "riftHeralds", "barons", "dragons", "nexus"]
        table.non_pk_args = []
    return table
