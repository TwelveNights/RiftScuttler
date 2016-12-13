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
    nav_list_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_raw]
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
    nav_list_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_raw]
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
    nav_list_raw = get_nav_list_raw()
    nav_list_add = [("add-" + tables, "Add " + tables.title()) for tables in nav_list_raw]
    nav_list_remove = [("remove-" + tables, "Remove " + tables.title()) for tables in nav_list_raw]
    nav_list_edit = [("edit-" + tables, "Edit " + tables.title()) for tables in nav_list_raw]
    nav_list_view = [("view-" + tables, "View " + tables.title()) for tables in nav_list_raw]
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


def check_page_and_return_table(request):
    abs_url = request.get_full_path()
    list_of_tables = parse_tables()
    for i, table in enumerate(list_of_tables[0]):
        if abs_url.find("_"+table.tname+"/") != -1:
            return table
    return
