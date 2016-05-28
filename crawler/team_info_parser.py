import consts
from consts import queries
import requests
import lxml.html
from utils import normalize_string

class Team:
    def __init__(self, url):
        self.tree = lxml.html.fromstring(
            requests.get(url, headers=consts.HEADERS).text
            )
        self.name = ''
        self.url_profile = url
        self.manager_url = ''
        self.players_urls = []
  
