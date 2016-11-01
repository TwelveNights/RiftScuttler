from os import getcwd
from django.db import migrations

def set_operations(operations, *names):
    sql_files = [getcwd() + "/common/sql/" + n + ".sql" for n in names]

    for sql in sql_files:
        with open(sql, 'r') as cmds:
            operations.append(migrations.RunSQL(cmds.read()))
