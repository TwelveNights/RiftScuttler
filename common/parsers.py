import json

def parse_data(func, data, file_name):
    "Parses data for static data"

    reader = json.JSONDecoder()
    json_data = reader.decode(data)["data"]

    with open(file_name, 'w') as sql:
        for k, v in json_data.items():
            value = func(k, v)
            if value is not None:
                sql.write(func(k, v))

        sql.close()

def retrieve_champions(key, value):
    "Parses data for static champion data"

    name = value["name"].replace("'", "''")
    return "INSERT INTO champions VALUES ({0}, '{1}');\n".format(key, name)

def retrieve_items(key, value):
    "Parses data for static item data"

    if "name" in value:
        name = value["name"].replace("'", "''")
        return "INSERT INTO items VALUES ({0}, '{1}');\n".format(key, name)

    return None
