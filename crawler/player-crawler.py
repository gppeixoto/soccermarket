import lxml.html
from selenium import webdriver
from consts import *
from utils import *

def crawlPlayersUrls():
    driver = webdriver.Firefox()
    driver.get(PLAYER_SEEDS)
    playerUrls = []
    for i in xrange(2, 17):
        time.sleep(30)
        source = driver.page_source
        tree = lxml.html.fromstring(source)
        res = tree.xpath('//a[@class="spielprofil_tooltip"]')
        for player in res:
            playerUrls.append(player.get("href"))
        print playerUrls
        nextPage = "http://www.transfermarkt.co.uk/premier-league/marktwertaenderungen/wettbewerb/GB1/pos//detailpos/0/plus/1/page/{0}".format(i)
        driver.get(nextPage)
    with open("playersUrls.csv", "w") as outfile:
        for url in playerUrls:
            outfile.write(url+"\n")
