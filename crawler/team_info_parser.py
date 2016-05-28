import consts
import requests
import lxml.html

class Team:
    def __init__(self, url):
        self.tree = lxml.html.fromstring(
            requests.get(url, headers=consts.HEADERS).text
            )
        self.url_profile = url
        self.name = ''
        self.country = ''
        self.badge = ''
        self.coach_url = ''
        self.kit_image = ''
        self.full_name = ''
        self.players_urls = []
        self.players = []

    def parse_full_name(self):
        self.full_name = self.tree.xpath('//div[@class="spielername-profil"]')[0]\
                                .getchildren()[0]\
                                .text

    def parse_badge(self):
        self.badge = self.tree.xpath('//div[@class="headerfoto"]')[0]\
                                .getchildren()[0]\
                                .get("src")

    def parse_country(self):
        self.country = self.tree.xpath('//td[@itemprop="addressLocality"]')[0]\
                                .text

    def parse_coachUrl(self):
        self.coach_url = self.tree.xpath('//div[@class="container-hauptinfo"]')[0]\
                                .get("href")

    def parse_players_urls(self):
        response = self.tree.xpath(consts.queries["team_players"])
        self.players_urls = [res.get('href') for res in response]

    def parse_info(self):
        self.parse_full_name()
        self.parse_badge()
        self.parse_country()
        self.parse_coachUrl()
        self.parse_players_urls()

    def to_csv(self):
        csv = ",".join([\
            self.full_name,\
            self.badge,\
            self.country,\
            self.url_profile,\
            str(self.players_urls)
        ])
        return csv
