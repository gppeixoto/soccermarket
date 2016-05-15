import consts
from consts import queries
import requests
import lxml.html
from utils import normalize_string

class Manager:
    def __init__(self, url):
        self.tree = lxml.html.fromstring(
            requests.get(url, headers=consts.HEADERS).text
            )
        self.url_profile = url
        self.name = ''
        self.age = ''
        self.nationality = ''
        self.win_percentage = ''
        self.preferred_formation = ''

    def parse_info(self):
        rows = self.get_info_table().findall('tr')
        rows = map(lambda row: row.find('th'), rows)
        for row in rows:
            self.parse_row(row)

    def get_info_table(self):
        table = self.tree.xpath('//table[@class="auflistung"]')[0]
        return table

    def parse_row(self, row):
        text = normalize_string(row.text)
        sibling = row.getnext()
        if 'name' in text:
            self.name = normalize_string(sibling.text)
        elif 'age' in text and len(text)<=4:
            self.age = sibling.text
        elif 'nationality' in text:
            nationality = sibling.find('img').get('alt')
            self.nationality = normalize_string(nationality)
        elif 'formation' in text:
            self.preferred_formation = sibling.text
        elif 'success rate' in text:
            self.win_percentage = sibling.\
                    xpath(queries["win_percentage"])[0]\
                    .text\
                    .replace(',', '.')

    def to_csv(self):
        csv = ",".join([self.name, self.age, self.nationality,\
                        self.win_percentage, self.preferred_formation])
        return csv
