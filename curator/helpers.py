from .tables import *
from django.db import transaction, IntegrityError


def insert_data(cursor, table):
    sql = "INSERT INTO " + table.tname + " VALUES ("
    length_args = len(table.args)
    for i, args in enumerate(table.args):
        sql += "'" + str(args) + "'"
        if i == (length_args - 1):
            break
        sql += ", "
    sql += ")"
    try:
        cursor.execute(sql, [])
        transaction.commit()
    except IntegrityError as e:
        return str(e)


def delete_data(cursor, table):
    sql = "DELETE FROM " + table.tname + " WHERE "
    pk_length = len(table.pk)
    for i, pk in enumerate(table.pk):
        sql += pk[0] + "="
        sql += "'" + str(table.args[i]) + "'"
        if i == (pk_length - 1):
            break
        sql += " AND "
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.execute(sql, [])
    transaction.commit()


def edit_data(cursor, table):
    sql = "UPDATE " + table.tname + " SET "
    pk_length = len(table.pk)
    non_pk_length = len(table.non_pk)
    for j, col in enumerate(table.non_pk):
        sql += col[0] + "=" + "'" + str(table.non_pk_args[j]) + "'"
        if j < (non_pk_length - 1):
            sql += ", "
    sql += " WHERE "
    for i, pk in enumerate(table.pk):
        sql += pk[0] + "="
        sql += "'" + str(table.args[i]) + "'"
        if i == (pk_length - 1):
            break
        sql += " AND "

    try:
        cursor.execute(sql, [])
        transaction.commit()
    except IntegrityError as e:
        return str(e)


def check_if_pk_exists(cursor, table):
    sql = "SELECT * FROM "
    sql += table.tname
    sql += " WHERE "
    for i, pk in enumerate(table.pk):
        sql += pk[0] + "=" + "'" + str(table.args[i]) + "'"
        if i == len(table.pk)-1:
            break
        sql += " AND "
    cursor.execute(sql, [])
    data = cursor.fetchall()
    return bool(data)


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
    return [cols[0] for cols in column_list]


def create_context(request, table, form, list_of_data, args, e):
    value = table.tname.title()
    nav_list_raw = get_nav_list_raw()
    nav_list_edit_raw = get_nav_list_edit_raw()
    nav_list_add = [("add-"+tables, "Add "+tables.title()) for tables in nav_list_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_raw]
    nav_list_edit = [("edit-" + tables2, "Edit " + tables2.title()) for tables2 in nav_list_edit_raw]
    abs_url = request.get_full_path()
    if abs_url.find("/add_") != -1:
        method = "Add"
    elif abs_url.find("/remove_") != -1:
        method = "Remove"
    elif abs_url.find("/edit_") != -1:
        method = "Edit"
    nav_list = [(nav_list_add, "Add"), (nav_list_remove, "Remove"), (nav_list_edit, "Edit")]
    context = {
        "form": form,
        "object_list": list_of_data,
        "title": value,
        "args": args,
        "nav_list": nav_list,
        "method": method,
        "error": e,
    }
    return context


def create_context_index():
    nav_list_raw = get_nav_list_raw()
    nav_list_edit_raw = get_nav_list_edit_raw()
    nav_list_add = []
    nav_list_remove = []
    nav_list_edit = []

    for i, table in enumerate(nav_list_raw):
        nav_list_add.append(("add-"+table, "Add "+table.title()))

    for i, table in enumerate(nav_list_raw):
        nav_list_remove.append(("remove-" + table, "Remove " + table.title()))

    for i, table2 in enumerate(nav_list_edit_raw):
        nav_list_edit.append(("edit-" + table2, "Edit " + table2.title()))
    nav_list = [(nav_list_add, "Add"), (nav_list_remove, "Remove"), (nav_list_edit, "Edit")]
    context = {
        "welcome": "Welcome to the curator's home page.",
        "nav_list": nav_list,
    }
    return context


def get_nav_list_raw():
    nav_list_raw = ["tournaments", "series", "champions", "items", "players", "teams", "matches", "bans", "organizes",
                    "competes", "interacts", "participates", "plays", "registers", "scores"]
    return nav_list_raw


def get_nav_list_edit_raw():
    nav_list_edit_raw = ["tournaments", "series", "champions", "items", "players", "teams", "matches",
                         "organizes", "competes", "interacts", "participates", "plays", "registers", "scores"]
    return nav_list_edit_raw


def get_non_pk_args(table):
    args = []
    pk_length = len(table.pk)
    for i, cols in enumerate(table.cols):
        if i >= pk_length:
            args.append(table.args[i])
    return args


def label_cols_with_pk(table):
    list_of_cols_with_pk = []
    for i, cols in enumerate(table.pk):
        list_of_cols_with_pk.append([cols[0], cols[1], "pk"])
    for j, cols in enumerate(table.non_pk):
        list_of_cols_with_pk.append([cols[0], cols[1], "non-pk"])
    return list_of_cols_with_pk


def create_reverse_name_add(table_name):
    name = "add-" + table_name
    return name


def create_reverse_name_remove(table_name):
    name = "remove-" + table_name
    return name


def create_reverse_name_edit(table_name):
    name = "edit-" + table_name
    return name


def check_page_and_return_table(request):
    abs_url = request.get_full_path()
    table = StructData()
    if abs_url.find("_tournaments/") != -1:
        table.tname = "tournaments"
        table.cols = [("id", "charfield16"), ("name", "charfield256"), ("year", "int"), ("location", "text")]
        table.args = []
        table.pk = [("id", "charfield16")]
        table.non_pk = [("name", "charfield256"), ("year", "int"), ("location", "text")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_series/") != -1:
        table.tname = "series"
        table.cols = [("id", "int"), ("bestOfCount", "int")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = [("bestOfCount", "int")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_champions/") != -1:
        table.tname = "champions"
        table.cols = [("id", "int"), ("name", "charfield16")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = [("name", "charfield16")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_items/") != -1:
        table.tname = "items"
        table.cols = [("id", "int"), ("name", "text")]
        table.args = []
        table.pk = [("id", "int")]
        table.non_pk = [("name", "text")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_players/") != -1:
        table.tname = "players"
        table.cols = [("name", "charfield16"), ("careerStartDate", "datetime")]
        table.args = []
        table.pk = [("name", "charfield16")]
        table.non_pk = [("careerStartDate", "datetime")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_teams/") != -1:
        table.tname = "teams"
        table.cols = [("id", "charfield6"), ("region", "charfield2"), ("name", "text")]
        table.args = []
        table.pk = [("id", "charfield6")]
        table.non_pk = [("region", "charfield2"), ("name", "text")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_matches/") != -1:
        table.tname = "matches"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("date", "datetime")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int")]
        table.non_pk = [("date", "datetime")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_bans/") != -1:
        table.tname = "bans"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("championID", "int"), ("pickTurn", "int")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("championID", "int")]
        table.non_pk = []
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_organizes/") != -1:
        table.tname = "organizes"
        table.cols = [("tournamentID", "charfield256"), ("seriesID", "int"), ("stage", "text")]
        table.args = []
        table.pk = [("tournamentID", "int"), ("seriesID", "int")]
        table.non_pk = [("stage", "text")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_competes/") != -1:
        table.tname = "competes"
        table.cols = [("seriesID", "int"), ("teamID", "charfield6"), ("blueSide", "boolean")]
        table.args = []
        table.pk = [("seriesID", "int"), ("teamID", "charfield6")]
        table.non_pk = [("blueSide", "boolean")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_interacts/") != -1:
        table.tname = "interacts"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("itemID", "int"),
                      ("time", "int"), ("isBuy", "int")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("playerID", "int"), ("itemID", "int"),
                    ("time", "int")]
        table.non_pk = [("isBuy", "int")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_participates/") != -1:
        table.tname = "participates"
        table.cols = [("tournamentID", "charfield256"), ("teamID", "charfield6"), ("stageReached", "text")]
        table.args = []
        table.pk = [("tournamentID", "charfield256"), ("teamID", "charfield6")]
        table.non_pk = [("stageReached", "text")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_plays/") != -1:
        table.tname = "plays"
        table.cols = [("seriesID", "int"), ("matchNumber", "int"), ("player", "charfield16"),
                      ("championID", "int"), ("role", "charfield6"), ("kills", "int"), ("deaths", "int"),
                      ("assists", "int"), ("damageDealt", "int"), ("wardsPlaced", "int"), ("wardsDestroyed", "int"),
                      ("cs", "int"), ("teamJungleMinions", "int"), ("enemyJungleMinions", "int"), ("gold", "int")]
        table.args = []
        table.pk = [("seriesID", "int"), ("matchNumber", "int"), ("player", "charfield16"),
                    ("championId", "charfield16")]
        table.non_pk = [("role", "charfield6"), ("kills", "int"), ("deaths", "int"), ("assists", "int"),
                        ("damageDealt", "int"), ("wardsPlaced", "int"), ("wardsDestroyed", "int"),
                        ("cs", "int"), ("teamJungleMinions", "int"), ("enemyJungleMinions", "int"), ("gold", "int")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_registers/") != -1:
        table.tname = "registers"
        table.cols = [("playerID", "int"), ("teamID", "charfield6"), ("dateJoined", "date"),
                      ("dateLeft", "date")]
        table.args = []
        table.pk = [("playerID", "int"), ("teamID", "charfield6")]
        table.non_pk = [("dateJoined", "date"), ("dateLeft", "date")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    elif abs_url.find("_scores/") != -1:
        table.tname = "scores"
        table.cols = [("teamID", "charfield6"), ("seriesID", "int"), ("matchNumber", "int"),
                      ("inhibitors", "int"), ("towers", "int"), ("riftHeralds", "int"), ("barons", "int"),
                      ("dragons", "int"), ("nexus", "int")]
        table.args = []
        table.pk = [("teamID", "charfield6"), ("seriesID", "int"), ("matchNumber", "int")]
        table.non_pk = [("inhibitors", "int"), ("towers", "int"), ("riftHeralds", "int"), ("barons", "int"),
                        ("dragons", "int"), ("nexus", "int")]
        table.non_pk_args = []
        table.pk_labeled_cols = []
    return table
