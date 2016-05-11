import consts
import requests

class Player:
    def __init__(self, url):
        self.url_profile = url
        self.age = 0
        self.name = ''
        self.nationality = ''
        self.position = ''
        self.foot = 'R'
        self.market_value = 0
        self.shirt_number = 0
        self.agent = ''


    def get_info_table(self):
        headers = {'User-Agent': consts.USER_AGENT}
        tree = lxml.html.fromstring(requests.get(self.url_profile, headers=headers).text)
        infoTable = tree.xpath('//table[@class="auflistung"]')
        if infoTable:
            infoTable = infoTable[0]
        return infoTable

    def parse_row(self, i, row):
        if i == 0:
            self.name = row.text.strip()
        elif i == 1:
            self.dob = row.getchildren()[0].text.strip()
        elif i == 2:
            self.pob = row.find('span').text.strip()
        elif i == 3:
            self.age = int(row.text)
        elif i == 4:
            self.height = row.text.strip()
        elif i == 5:
            self.nationality = row.find('img').get('alt')
        elif i == 6:
            self.position = row.text.strip()
        elif i == 7:
            self.


    def parse_info(self):
        rows = self.get_info_table().findall('tr')
        rows = [row.find('td') for row in rows]
        for i, row in enumerate(rows):
            self.parse_row(i, row)
