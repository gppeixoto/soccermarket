import consts
import requests
import lxml.html

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
        self.agent = ''
        self.parse_info()

    def parse_market_value(self):
        self.market_value = self.tree.xpath('//div[@class="right-td"]')[0]\
                                .getchildren()[0]\
                                .text
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
            self.nationality = row.find('img').get('alt')
        elif i == 6:
            self.position = row.text.strip()
        elif i == 7:
            self.foot = row.text.strip()
        elif i == 8:
            self.agent = row.getchildren()[0].text


    def parse_info(self):
        rows = self.get_info_table().findall('tr')
        rows = map(lambda row: row.find('td'), rows)
        for i, row in enumerate(rows):
            self.parse_row(i, row)
        self.parse_market_value()
        self.parse_jersey_number()

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
