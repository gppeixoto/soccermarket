import consts
from consts import queries
import requests
import lxml.html

"""
preferred_formation = models.CharField(max_length = 10)
win_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
"""
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
        text = row.text.strip().lower()
        sibling = row.getnext()
        if 'name' in text:
            self.name = sibling.text
        elif 'age' in text:
            self.age = sibling.text
        elif 'nationality' in text:
            self.nationality = sibling.text
        elif 'formation' in text:
            self.preferred_formation = sibling.text
        elif 'success rate' in text:
            self.win_percentage = sibling.xpath(queries["win_percentage"])[0].text

    def to_csv(self):
        csv = ",".join([self.name, self.age, self.nationality,\
                        self.win_percentage, self.preferred_formation])
        return csv
