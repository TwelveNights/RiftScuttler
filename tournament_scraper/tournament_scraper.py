import subprocess
import sys
import json
import re
from bs4 import BeautifulSoup

class Parser:
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
        args=[ 'python', 'render.py', url, self.dump_file ]
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
                self.match_details.append({'parent_url' : url, 'link' : h})
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
    if len(sys.argv) > 2 :
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

    parser = Parser(dump_file, url_queue_file, seen_url_file, match_data_file, do_load)
    parser.parse_it(starter_url)
