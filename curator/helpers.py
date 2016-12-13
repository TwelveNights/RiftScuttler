from django.db import connection, transaction, IntegrityError
from .table_parsers import parse_tables


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
    except IntegrityError or Warning as e:
        return str(e)


def delete_data(cursor, table):
    sql = "DELETE FROM " + table.tname + " WHERE "
    count = count_pk(table)
    for i, cols in enumerate(table.cols):
        sql += cols[0] + "="
        sql += "'" + str(table.args[i]) + "'"
        if i == count[0]-1:
            break
        sql += " AND "
    try:
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute(sql, [])
        transaction.commit()
    except IntegrityError or Warning as e:
        return str(e)


def edit_data(cursor, table):
    sql = "UPDATE " + table.tname + " SET "
    count = count_pk(table)
    for j, cols in enumerate(table.cols):
        if cols[2] == "non-pk":
            sql += cols[0] + "=" + "'" + str(table.args[j]) + "'"
            if j < (count[1]+count[0] - 1):
                sql += ", "
    sql += " WHERE "
    for i, cols in enumerate(table.cols):
        sql += cols[0] + "="
        sql += "'" + str(table.args[i]) + "'"
        if i == (count[0] - 1):
            break
        sql += " AND "
    try:
        cursor.execute(sql, [])
        transaction.commit()
    except IntegrityError or Warning as e:
        return str(e)


def select_data(cursor, tname):
    sql = "SELECT * FROM "
    sql += tname
    cursor.execute(sql, [])
    list_of_data = cursor.fetchall()
    return list_of_data


def select_data_with_pk(cursor, table):
    sql = "SELECT * FROM "
    sql += table.tname
    sql += " WHERE "
    count = count_pk(table)
    for i, cols in enumerate(table.cols):
        sql += cols[0] + "=" + "'" + str(table.args[i]) + "'"
        if i == count[0]-1:
            break
        sql += " AND "
    try:
        cursor.execute(sql, [])
        data = cursor.fetchone()
        return data
    except IntegrityError as e:
        return str(e)


def count_pk(table):
    pk_count = 0
    non_pk_count = 0
    for cols in table.cols:
        if cols[2] == "pk":
            pk_count += 1
        else:
            non_pk_count += 1
    return [pk_count, non_pk_count]


def filter_cols_with_pk(cols):
    pk = []
    for col in cols:
        if col[2] == "pk":
            pk.append(col)
        else:
            break
    return pk


def reorder_dictionary(table):
    new_table_args = []
    for i, cols in enumerate(table.cols):
        for j, args in enumerate(table.args):
            if cols[0] == args[0]:
                new_table_args.append(args[1])
                break
    return new_table_args


def check_and_replace_none(table):
    cursor = connection.cursor()
    data = select_data_with_pk(cursor, table)
    for i, args in enumerate(table.args):
        if args is None:
            table.args[i] = data[i]
    return table.args


def get_args(column_list):
    return [cols[0] for cols in column_list]


def create_context(request, table, form, e):
    cursor = connection.cursor()
    list_of_data = select_data(cursor, table.tname)
    connection.close()
    args = get_args(table.cols)
    abs_url = request.get_full_path()
    nav_list_form_raw = get_nav_list_raw()
    nav_list_view_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_form_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_form_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_form_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_view_raw]
    nav_list = [(nav_list_view, "View"), (nav_list_add, "Add"), (nav_list_remove, "Remove"), (nav_list_edit, "Edit")]
    value = table.tname.title()
    if abs_url.find("/add_") != -1:
        method = "Add"
    elif abs_url.find("/remove_") != -1:
        method = "Remove"
    elif abs_url.find("/edit_") != -1:
        method = "Edit"
    elif abs_url.find("/view_") != -1:
        method = "View"
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


def create_context_view(request, table):
    cursor = connection.cursor()
    list_of_data = select_data(cursor, table.tname)
    connection.close()
    args = get_args(table.cols)
    abs_url = request.get_full_path()
    nav_list_form_raw = get_nav_list_raw()
    nav_list_view_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_form_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_form_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_form_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_view_raw]
    nav_list = [(nav_list_view, "View"), (nav_list_add, "Add"), (nav_list_remove, "Remove"), (nav_list_edit, "Edit")]
    value = table.tname.title()
    if abs_url.find("/add_") != -1:
        method = "Add"
    elif abs_url.find("/remove_") != -1:
        method = "Remove"
    elif abs_url.find("/edit_") != -1:
        method = "Edit"
    elif abs_url.find("/view_") != -1:
        method = "View"
    context = {
        "object_list": list_of_data,
        "title": value,
        "args": args,
        "nav_list": nav_list,
        "method": method,
    }
    return context


def create_context_index():
    nav_list_form_raw = get_nav_list_raw()
    nav_list_view_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_form_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_form_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_form_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_view_raw]
    nav_list = [(nav_list_view, "View"), (nav_list_add, "Add"), (nav_list_remove, "Remove"), (nav_list_edit, "Edit")]
    context = {
        "welcome": "Welcome to the curator's home page.",
        "nav_list": nav_list,
    }
    return context


def create_reverse_name(request, table_name):
    abs_url = request.get_full_path()
    name = ""
    if abs_url.find("/add_") != -1:
        name = "add-" + table_name
        return name
    elif abs_url.find("/remove_") != -1:
        name = "remove-" + table_name
    elif abs_url.find("/edit_") != -1:
        name = "edit-" + table_name
    return name


def get_nav_list_raw():
    table_info = parse_tables()
    return table_info[1]


def get_nav_list_form_raw():
    nav_list_raw = get_nav_list_raw()
    return nav_list_raw


def get_nav_list_view_raw():
    nav_list_raw = get_nav_list_raw()
    return nav_list_raw




def check_page_and_return_table(request):
    abs_url = request.get_full_path()
    list_of_tables = parse_tables()
    for i, table in enumerate(list_of_tables[0]):
        if abs_url.find("_"+table.tname+"/") != -1:
            return table
    return

"""
def check_page_and_return_table2(request):
    abs_url = request.get_full_path()
    table = Table()
    if abs_url.find("_tournaments/") != -1:
        table.tname = "tournaments"
        table.cols = [("id", "charfield16", "pk"), ("name", "charfield256", "non-pk"), ("year", "int", "non-pk"),
                      ("location", "text", "non-pk")]
        table.args = []
    elif abs_url.find("_series/") != -1:
        table.tname = "series"
        table.cols = [("id", "int", "pk"), ("bestOfCount", "int", "non-pk")]
        table.args = []
    elif abs_url.find("_champions/") != -1:
        table.tname = "champions"
        table.cols = [("id", "int", "pk"), ("name", "charfield16", "non-pk")]
        table.args = []
    elif abs_url.find("_items/") != -1:
        table.tname = "items"
        table.cols = [("id", "int", "pk"), ("name", "text", "non-pk")]
        table.args = []
    elif abs_url.find("_players/") != -1:
        table.tname = "players"
        table.cols = [("name", "charfield16", "pk"), ("careerStartDate", "date", "non-pk")]
        table.args = []
    elif abs_url.find("_teams/") != -1:
        table.tname = "teams"
        table.cols = [("id", "charfield6", "pk"), ("region", "charfield2", "non-pk"), ("name", "text", "non-pk")]
        table.args = []
    elif abs_url.find("_matches/") != -1:
        table.tname = "matches"
        table.cols = [("seriesID", "int", "pk"), ("matchNumber", "int", "pk"), ("date", "date", "non-pk")]
        table.args = []
    elif abs_url.find("_bans/") != -1:
        table.tname = "bans"
        table.cols = [("seriesID", "int", "pk"), ("matchNumber", "int", "pk"), ("championID", "int", "pk"),
                      ("pickTurn", "int", "non-pk")]
        table.args = []
    elif abs_url.find("_organizes/") != -1:
        table.tname = "organizes"
        table.cols = [("tournamentID", "charfield256", "pk"), ("seriesID", "int", "pk"), ("stage", "text", "non-pk")]
        table.args = []
    elif abs_url.find("_competes/") != -1:
        table.tname = "competes"
        table.cols = [("seriesID", "int", "pk"), ("teamID", "charfield6", "pk"), ("blueSide", "boolean", "non-pk")]
        table.args = []
    elif abs_url.find("_interacts/") != -1:
        table.tname = "interacts"
        table.cols = [("seriesID", "int", "pk"), ("matchNumber", "int", "pk"), ("player", "charfield16", "pk"),
                      ("itemID", "int", "pk"), ("time", "int", "pk"), ("isBuy", "int", "non-pk")]
        table.args = []
    elif abs_url.find("_participates/") != -1:
        table.tname = "participates"
        table.cols = [("tournamentID", "charfield256", "pk"), ("teamID", "charfield6", "pk"),
                      ("stageReached", "text", "non-pk")]
        table.args = []
    elif abs_url.find("_plays/") != -1:
        table.tname = "plays"
        table.cols = [("seriesID", "int", "pk"), ("matchNumber", "int", "pk"), ("player", "charfield16", "pk"),
                      ("championID", "int", "pk"), ("role", "charfield6", "non-pk"), ("kills", "int", "non-pk"),
                      ("deaths", "int", "non-pk"), ("assists", "int", "non-pk"), ("damageDealt", "int", "non-pk"),
                      ("wardsPlaced", "int", "non-pk"), ("wardsDestroyed", "int", "non-pk"), ("cs", "int", "non-pk"),
                      ("teamJungleMinions", "int", "non-pk"), ("enemyJungleMinions", "int", "non-pk"),
                      ("gold", "int", "non-pk")]
        table.args = []
    elif abs_url.find("_registers/") != -1:
        table.tname = "registers"
        table.cols = [("playerID", "charfield16", "pk"), ("teamID", "charfield6", "pk"), ("dateJoined", "date", "non-pk"),
                      ("dateLeft", "date", "non-pk")]
        table.args = []
    elif abs_url.find("_scores/") != -1:
        table.tname = "scores"
        table.cols = [("teamID", "charfield6", "pk"), ("seriesID", "int", "pk"), ("matchNumber", "int", "pk"),
                      ("inhibitors", "int", "non-pk"), ("towers", "int", "non-pk"), ("riftHeralds", "int", "non-pk"),
                      ("barons", "int", "non-pk"), ("dragons", "int", "non-pk"), ("nexus", "int", "non-pk")]
        table.args = []
    elif abs_url.find("_wins/") != -1:
        table.tname = "wins"
        table.cols = [("teamID", "charfield6", "pk"), ("wins", "int", "non-pk")]
        table.args = []
    return table

"""
