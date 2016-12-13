from os import getcwd
from .tables import Table
import sqlparse
import sys


def anaconda3_parser(parsed, i, j, val):
    if (parsed[i].tokens[j].ttype is None
        and parsed[i].tokens[j - 2].ttype in sqlparse.tokens.Keyword
        and parsed[i].tokens[j - 2].value.upper() == 'TABLE'
        and parsed[i].tokens[j - 4].ttype in sqlparse.tokens.Keyword
        and parsed[i].tokens[j - 4].value.upper() == 'CREATE'):
        content = str(val)
        return [content]
    return None


def python3_parser(parsed, i, j):
    if (parsed[i].tokens[j].ttype is None
        and parsed[i].tokens[j - 2].ttype in sqlparse.tokens.Keyword
        and parsed[i].tokens[j - 2].value.upper() == 'TABLE'
        and parsed[i].tokens[j - 4].ttype in sqlparse.tokens.Keyword
        and parsed[i].tokens[j - 4].value.upper() == 'CREATE'):
        content = str(parsed[i].tokens[j+2])
        return [content, str(parsed[i].tokens[j])]
    return None


def anaconda3_generate_table_names(list_of_table_names, content):
    table_name = ""
    for k, letter in enumerate(content):
        if letter == " ":
            break
        table_name += content[k]
    list_of_table_names.append(table_name)
    return list_of_table_names


def python3_generate_table_names(list_of_table_names, table_name_string):
    list_of_table_names.append(table_name_string)
    return list_of_table_names


def parse_tables():
    list_of_tables = []
    list_of_table_names = []
    list_of_cols_final = []
    list_of_pk_final = []
    # list_of_checks = []
    # list_of_checks_final = []
    sql_script = getcwd() + "/common/sql/000_create_tables.sql"
    sql = open(sql_script, 'r')
    parsed = sqlparse.parse(sql)
    for i, stmt in enumerate(parsed):
        for j, val in enumerate(stmt.tokens):
            if 'conda' in sys.version:
                content = anaconda3_parser(parsed, i, j, val)
                if content is None:
                    continue
                content = content[0]
                list_of_table_names = anaconda3_generate_table_names(list_of_table_names, content)
            else:
                content = python3_parser(parsed, i, j)
                if content is None:
                    continue
                table_name_string = content[1]
                content = content[0]
                list_of_table_names = python3_generate_table_names(list_of_table_names, table_name_string)

            text = content.split()

            """
            for k, entry in enumerate(text):
                if entry == 'CHECK':
                    list = [(text[k+1],text[k+2],text[k+3])]
                    if text[k+4] == 'OR':
                        list.append((text[k+5],text[k+6],text[k+7]))
                    list_of_checks.append(list)
            """

            list_of_pk = extract_pk(text)
            list_of_pk_final.append(list_of_pk)

            text = remove_irrelevant(text)
            list_of_cols = []
            for k, entry in enumerate(text):
                if entry == 'end':
                    continue
                elif 'conda' in sys.version and text[k-1] == 'end':
                    continue
                else:
                    list_of_cols.append(entry)
            list_of_cols2 = []

            for k, word in enumerate(list_of_cols):
                if word == 'NULL' or word == 'NULL,':
                    continue
                elif ',' in word:
                    new_word = word[:-1]
                    list_of_cols2.append(new_word)
                else:
                    list_of_cols2.append(word)
            list_of_cols_final.append(list_of_cols2)

    for k, row in enumerate(list_of_cols_final):
        table = Table()
        table.tname = list_of_table_names[k]
        table.cols = []
        for p, entry in enumerate(row):
            if p % 2 == 1:
                continue
            cols = (entry, row[p+1], 'non-pk')
            pk_row = list_of_pk_final[k]
            for n, pk in enumerate(pk_row):
                if entry == pk:
                    cols = (entry, row[p+1], 'pk')
                    break
            table.cols.append(cols)
        list_of_tables.append(table)

    """
        for i, list in enumerate(list_of_checks):
        temp_list = []
        for j, tuple in enumerate(list):
            for k, entry in enumerate(tuple):
                if '(' in entry:
                    temp1 = entry[1:]
                if '),' in entry:
                    temp3 = entry[:-2]
                if k == 1:
                    temp2 = entry
            temp_list.append((temp1, temp2, temp3))
        list_of_checks_final.append(temp_list)
    """
    return [list_of_tables, list_of_table_names]


def extract_pk(text):
    for i, entry in enumerate(text):
        if entry.upper() == 'PRIMARY':
            text = text[i:]
    for i, entry in enumerate(text):
        if entry == ')':
            text = text[:i]
    for i, entry in enumerate(text):
        if entry.upper() == 'FOREIGN':
            text = text[:i]
    del text[0]
    del text[0]
    list_of_words = []
    for i, word in enumerate(text):
        if '(' in word and ')' in word:
            new_word = word[1:-1]
            list_of_words.append(new_word)
        elif '(' in word:
            new_word = word[1:-1]
            list_of_words.append(new_word)
        elif ')' in word:
            new_word = word[:-2]
            list_of_words.append(new_word)
        else:
            new_word = word[:-1]
            list_of_words.append(new_word)
    return list_of_words


def remove_irrelevant(text):
    for i, string in enumerate(text):
        if string.upper() == 'CHECK':
            text = text[:i]
            text.insert(i, "end")
    for i, string in enumerate(text):
        if string.upper() == 'PRIMARY':
            text = text[:i]
            text.insert(i, "end")
    for i, string in enumerate(text):
        if string == '(' or string == ')' or text[i] == 'NOT' or text[i] == 'UNIQUE,':
            text.remove(string)
    return text
