import urllib.request
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


#match_path is a url endpoint, for example TRLH1/1001890201?gameHash=6751c4ef7ef58654
def retrieve_match(seriesID, matchNumber, team1Id, team2Id, match_path):

    SQL_inserts = []

    match_url = 'https://acs.leagueoflegends.com/v1/stats/game/' + match_path

    raw_data = urllib.request.urlopen(match_url).read()
    raw_data = raw_data.decode('utf-8')
    json_data = json.loads(raw_data)

    split_path = match_path.split('?')
    timeline_url = 'https://acs.leagueoflegends.com/v1/stats/game/' + split_path[0] + '/timeline?' + split_path[1]
    raw_timeline = urllib.request.urlopen(timeline_url).read()
    raw_timeline = raw_data.decode('utf-8')
    json_timeline = json.loads(raw_timeline)

    #SCORES
    t1_data = json_data['teams'][0]
    t1_inhibitors = t1_data['inhibitorKills']
    t1_towers = t1_data['towerKills']
    t1_riftHeralds = t1_data['riftHeraldKills']
    t1_barons = t1_data['baronKills']
    t1_dragons = t1_data['dragonKills']
    t1_nexus = 1 if (t1_data['win'] == 'Win') else 0

    t2_data = json_data['teams'][1]
    t2_inhibitors = t2_data['inhibitorKills']
    t2_towers = t2_data['towerKills']
    t2_riftHeralds = t2_data['riftHeraldKills']
    t2_barons = t2_data['baronKills']
    t2_dragons = t2_data['dragonKills']
    t2_nexus = 1 if (t2_data['win'] == 'Win') else 0

    SQL_inserts.append("INSERT INTO scores VALUES({0}, {1}, {2}, {3},"
                       " {4}, {5}, {6}, {7}, {8})\n".format(team1Id, seriesID, matchNumber, t1_inhibitors, t1_towers,
                                                            t1_riftHeralds, t1_barons, t1_dragons, t1_nexus))
    SQL_inserts.append("INSERT INTO scores VALUES({0}, {1}, {2}, {3},"
                       " {4}, {5}, {6}, {7}, {8})\n".format(team2Id, seriesID, matchNumber, t2_inhibitors, t2_towers,
                                                            t2_riftHeralds, t2_barons, t2_dragons, t2_nexus))

    #BANS
    for ban in t1_data['bans']:
        SQL_inserts.append("INSERT INTO bans VALUES({0},{1},{2},{3}))\n".format(seriesID, matchNumber, ban['championId'],
                                                                                ban['pickTurn']))
    for ban in t2_data['bans']:
        SQL_inserts.append("INSERT INTO bans VALUES({0},{1},{2},{3}))\n".format(seriesID, matchNumber, ban['championId'],
                                                                                ban['pickTurn']))



    #PLAYS (players are listed by summonerName only)

    for p in json_data['participants']:
        p_name = pid_to_sname(json_data, p['participantId'])

        role = p['timeline']['role']
        lane = p['timeline']['lane']
        p_role = "NONE"
        if lane == 'TOP':
            p_role = "Top"
        elif lane == 'MIDDLE':
            p_role = "Mid"
        elif lane == 'JUNGLE':
            p_role = "Jungle"
        elif role == 'DUO_CARRY':
            p_role = "ADC"
        elif role == 'DUO_SUPPORT':
            p_role = "Support"

        pstats = p['stats']


        SQL_inserts.append("INSERT INTO plays VALUES({0}, {1}, {2}, "
                           "{3},{4}, {5}, "
                           "{6}, {7}, {8}, "
                           "{9}, {10}}, {11},"
                           "{12}, {13}, {14})\n".format(seriesID, matchNumber, p_name, p['championId'], p_role,
                                                        pstats['kills'], pstats['deaths'], pstats['assists'],
                                                        pstats['totalDamageDealtToChampions'], pstats['wardsPlaced'],
                                                        pstats['wardsDestroyed'],pstats['totalMinionsKilled'],
                                                        pstats['neutralMinionsKilledTeamJungle'],
                                                        pstats['neutralMinionsKilledEnemyJungle'], pstats['goldEarned']))


    #INTERACTS
        for frame in json_timeline['frames']:
            for e in frame['events']:
                is_buy = 1 if e['type'] == 'ITEM_PURCHASED' else 0

                SQL_inserts.append("INSERT INTO interacts VALUES ({0}, {1}, {2}, "
                                   "{3}, {4}, {5}, {6})\n".format(seriesID, matchNumber,
                                                                  pid_to_sname(json_data, e['participantId']),
                                                                  e['itemId'], e['timeStamp'], is_buy))

    return SQL_inserts

def pid_to_sname(json_object, pid):
    return json_object['participantIdentities'][pid - 1]['player']['summonerName']




