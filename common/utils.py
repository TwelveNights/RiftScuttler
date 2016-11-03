from os import getcwd
from django.db import migrations

def set_operations(operations, path, *names):
    "load the SQL scripts to be run"
    sql_files = [getcwd() + "/" + path + "/sql/" + n + ".sql" for n in names]

    for sql in sql_files:
        with open(sql, 'r') as cmds:
            operations.append(migrations.RunSQL(cmds.read()))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))
