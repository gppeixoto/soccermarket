import lxml.html
import time
from selenium import webdriver
from consts import *
from utils import *

def crawlTeamsUrls():
    driver = webdriver.Firefox()
    driver.get(TEAMS_SEED)
    teamsUrls = []
    for i in xrange(2, 6):
        time.sleep(30)
        source = driver.page_source
        tree = lxml.html.fromstring(source)
        '//td[@class="no-border-links hauptlink"]'
        line = tree.xpath('//td[@class="no-border-links hauptlink"]')
        for team in line:
            teamsUrls.append(team.getchildren()[0].get("href"))
        print teamsUrls
        nextPage = (TEAMS_SEED + "?page={0}").format(i)
        print "\n###nextPage: "+nextPage
        driver.get(nextPage)
    with open("../data/teamsUrls.csv", "w") as outfile:
        for url in teamsUrls:
            outfile.write(url+"\n")


crawlTeamsUrls()