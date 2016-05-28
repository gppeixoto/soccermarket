import consts
import requests
import lxml.html
from utils import get_team_id_from_url as get_id

class Transfer:
    def __init__(self, date, origin_id, dest_id, value):
        self.date = date
        self.origin_id = origin_id
        self.dest_id = dest_id
        self.value = value

    def __str__(self):
        return ",".join([date, str(origin_id), str(dest_id), value])

class Player:
    def __init__(self, url):
        self.tree = lxml.html.fromstring(
            requests.get(url, headers=consts.HEADERS).text
            )
        self.url_profile = url
        self.age = ''
        self.name = ''
        self.nationality = ''
        self.position = ''
        self.foot = 'R'
        self.market_value = ''
        self.shirt_number = ''
        self.agent = 'not informed'
        self.transfer_history = []

    def parse_market_value(self):
        self.market_value = self.tree.xpath('//div[@class="right-td"]')[0]\
                                .text.strip().encode("ascii", "ignore")

    def parse_jersey_number(self):
        nb = self.tree.xpath('//span[@class="dataRN"]')[0].text
        if nb.startswith("#"):
            nb = nb[1:]
        self.shirt_number = nb

    def get_info_table(self):
        headers = {'User-Agent': consts.USER_AGENT}
        infoTable = self.tree.xpath('//table[@class="auflistung"]')
        if infoTable:
            infoTable = infoTable[0]
        return infoTable

    def parse_row(self, i, row):
        if i == 0:
            self.name = row.text.strip()
        elif i == 3:
            self.age = row.text
        elif i == 5:
            nationality = row.find('img').get('alt')
            if nationality:
                self.nationality = nationality
        elif i == 6:
            self.position = row.text.strip()
        elif i == 7:
            self.foot = row.text.strip()
        elif i == 8:
            agent = row.getchildren()[0].text
            if agent is not None and agent != '':
                self.agent = agent

    def parse_transfer_history(self):
        transfers = self.tree.xpath("//tr[@class='zeile-transfer']")
        for transfer in transfers:
            date = transfer.xpath('td[@class="zentriert hide-for-small"]')[1]\
                            .text.strip()
            origin = transfer.xpath('*/a[@class="vereinprofil_tooltip"]')[2]\
                            .get('href')
            origin_id = get_id(origin)
            dest = transfer.xpath('*/a[@class="vereinprofil_tooltip"]')[5]\
                            .get('href')
            dest_id = get_id(dest)
            value = transfer.xpath('td[@class="zelle-abloese"]')[0].text\
                            .strip().encode('ascii', 'ignore')
            self.transfer_history.append(
                Transfer(date, origin_id, dest_id, value)
            )

    def parse_info(self):
        rows = self.get_info_table().findall('tr')
        rows = map(lambda row: row.find('td'), rows)
        for i, row in enumerate(rows):
            self.parse_row(i, row)
        self.parse_market_value()
        self.parse_jersey_number()
        self.parse_transfer_history()

    def to_csv(self):
        csv = ",".join([\
            self.name,\
            self.age,\
            self.nationality,\
            self.position,\
            self.foot,\
            self.market_value,\
            self.shirt_number,\
            self.agent,\
            self.url_profile\
        ])
        return csv
