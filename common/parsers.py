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
def retrieve_match(seriesID, matchNumber, date, team1, team2, match_path):
    match_url = 'https://acs.leagueoflegends.com/v1/stats/game/' + match_path

    raw_data = urllib.request.urlopen(match_url).read()
    raw_data = raw_data.decode('utf-8')
    json_data = json.loads(raw_data)

    #SCORES
    team1_data = json_data['teams'][0]
    team1_inhibitors = team1_data['inhibitorKills']
    team1_towers = team1_data['towerKills']
    team1_riftHeralds = team1_data['riftHeraldKills']
    team1_barons = team1_data['baronKills']
    team1_dragons = team1_data['dragonKills']
    team1_nexus = 1 if (team1_data['win'] == 'Win') else 0

    team2_data = json_data['teams'][1]
    team2_inhibitors = team2_data['inhibitorKills']
    team2_towers = team2_data['towerKills']
    team2_riftHeralds = team2_data['riftHeraldKills']
    team2_barons = team2_data['baronKills']
    team2_dragons = team2_data['dragonKills']
    team2_nexus = 1 if (team2_data['win'] == 'Win') else 0

    #BANS
    team1_bans = [b['championId'] for b in team1_data['bans']]
    team2_bans = [b['championId'] for b in team2_data['bans']]

    #PLAYS (players are listed by summonerName only)
    plays_list = []
    for participant in json_data['participants']:
        player = {}
        player['name'] = json_data['participantIdentities'][participant['participantId'] - 1]['player']['summonerName']
        player['champion'] = participant['championId']

        role = participant['timeline']['role']
        lane = participant['timeline']['lane']
        if lane == 'TOP':
            player['role'] = "Top"
        elif lane == 'MIDDLE':
            player['role'] = "Mid"
        elif lane == 'JUNGLE':
            player['role'] = "Jungle"
        elif role == 'DUO_CARRY':
            player['role'] = "ADC"
        else:
            player['role'] = "Support"

        pstats = participant['stats']
        player['kills'] = pstats['kills']
        player['deaths'] = pstats['deaths']
        player['assists'] = pstats['assists']
        player['damageDealt'] = pstats['totalDamageDealtToChampions']
        player['wardsPlaced'] = pstats['wardsPlaced']
        player['gold'] = pstats['goldEarned']

        plays_list.append(player)

    #INTERACTS (This information will have to be parsed from the match history HTML
        






