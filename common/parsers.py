import json
import sys
import re
import subprocess
from urllib import request
from bs4 import BeautifulSoup

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

    raw_data = request.urlopen(match_url).read()
    raw_data = raw_data.decode('utf-8')
    json_data = json.loads(raw_data)

    split_path = match_path.split('?')
    timeline_url = 'https://acs.leagueoflegends.com/v1/stats/game/' + split_path[0] + '/timeline?' + split_path[1]
    raw_timeline = request.urlopen(timeline_url).read()
    raw_timeline = raw_timeline.decode('utf-8')
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
        SQL_inserts.append("INSERT INTO bans VALUES({0},{1},{2},{3}))\n".format(seriesID, matchNumber, ban['championID'],
                                                                                ban['pickTurn']))
    for ban in t2_data['bans']:
        SQL_inserts.append("INSERT INTO bans VALUES({0},{1},{2},{3}))\n".format(seriesID, matchNumber, ban['championID'],
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
                           "{12}, {13}, {14})\n".format(seriesID, matchNumber, p_name, p['championID'], p_role,
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
                                   "{3}, {4}, {5})\n".format(seriesID, matchNumber,
                                                                  pid_to_sname(json_data, e['participantId']),
                                                                  e['itemId'], e['timeStamp'], is_buy))

    return SQL_inserts

def pid_to_sname(json_object, pid):
    return json_object['participantIdentities'][pid - 1]['player']['summonerName']


def crawl_tournament():
    sql_statements = []
    class Tournament_Parser:
        def __init__(self, dump_file, queue_file, seen_file, data_file, do_load):
            self.do_load = do_load
            self.dump_file = dump_file
            self.queue_file = queue_file
            self.seen_file = seen_file
            self.data_file = data_file
            self.urls = []
            self.seen_urls = []
            self.match_details = []

        def parse_it(self, url):
            starting_url = url
            if self.do_load:
                with open(self.queue_file, 'r', encoding='utf-8') as qf:
                    self.urls = json.load(qf)
                with open(self.seen_file, 'r', encoding='utf-8') as sf:
                    self.seen_urls = json.load(sf)
                with open(self.data_file, 'r', encoding='utf-8') as df:
                    self.match_details = json.load(df)
                self.do_load = False
                starting_url = self.urls.pop(0)

            print('Parsing {0}'.format(starting_url))
            self.seen_urls.append(starting_url)
            args = ['python', 'render.py', url, self.dump_file]
            # QT is a piece of sh*t library and prone to crashes, try it again
            # and dump progress to files if it can't recover:
            try:
                subprocess.check_call(args)
            except:
                print('Live! LIIIIVE!')
                try:
                    subprocess.check_call(args)
                except:
                    print('Snake? Snake?! SNAAAAAAAKE')
                    self.urls.append(url)
                    self.seen_urls.remove(url)
                    with open(self.queue_file, 'w', encoding='utf-8') as qf:
                        json.dump(self.urls, qf)
                    with open(self.seen_file, 'w', encoding='utf-8') as sf:
                        json.dump(self.seen_urls, sf)
                    with open(self.data_file, 'w', encoding='utf-8') as df:
                        json.dump(self.match_details, df)
                    print('Dumped progress to files, add file names and "True" to \
                           end of command line arguments and rerun.')
                    sys.exit(1)
            self.parse_helper(url)

        def parse_helper(self, url):
            global urls
            global seen_urls
            global match_data




            with open(self.dump_file, 'r', encoding='utf-8') as html_dump:
                html = html_dump.read()
            pfx = 'http://www.lolesports.com'
            soup = BeautifulSoup(html, 'html.parser')
            links = [link for link in soup.find_all('a')]

            for link in links:
                h = link.get('href')
                if h and re.search('matches/|schedule/', h):
                    if (pfx + h) not in self.seen_urls and (pfx + h) not in self.urls:
                        self.urls.append(pfx + h)
                elif h and 'match-details' in h:
                    print('Found match details for {0}'.format(url))
                    self.match_details.append({'parent_url': url, 'link': h})
                else:
                    continue
            if len(self.urls) > 0:
                self.parse_it(self.urls.pop(0))
            else:
                print('Found {0} match data'.format(len(self.match_details)))
                print('They are available in {0}'.format(self.data_file))
                with open(self.data_file, 'w', encoding='utf-8') as df:
                    json.dump(self.match_details, df)
                sys.exit(0)

    if __name__ == '__main__':
        starter_url = sys.argv[1]
        if len(sys.argv) > 2:
            dump_file = sys.argv[2]
        else:
            dump_file = 'html_dump.html'
        if len(sys.argv) > 3:
            url_queue_file = sys.argv[3]
        else:
            url_queue_file = 'url_queue.json'
        if len(sys.argv) > 4:
            seen_url_file = sys.argv[4]
        else:
            seen_url_file = 'seen_urls.json'
        if len(sys.argv) > 5:
            match_data_file = sys.argv[5]
        else:
            match_data_file = 'match_data.json'
        if len(sys.argv) > 6:
            do_load = sys.argv[6]
        else:
            do_load = False


        # url_bits = starter_url.split('/')
        # tournament_id = url_bits[5]
        #
        # sql_statements.append("INSERT INTO tournaments VALUES({0}, {1}, {2}, {3})\n".format())

        parser = Tournament_Parser(dump_file, url_queue_file, seen_url_file, match_data_file, do_load)
        parser.parse_it(starter_url)
        

