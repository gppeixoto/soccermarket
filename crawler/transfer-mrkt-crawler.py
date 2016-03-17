import time
import numpy as np
import lxml.html
from selenium import webdriver
from consts import queries
from consts import click_elem_path
from consts import SEED_URL

class Player:
    def __init__(self, img_url, name):
        self.img_url = img_url
        self.name = name

driver = webdriver.Firefox()
driver.get(SEED_URL)

for next_page in xrange(2, 11):
    time.sleep(30)
    source = driver.page_source
    tree = lxml.html(source)
    odds = tree.xpath(queries['odds'])
    evens = tree.xpath(queries['evens'])
    players = odds+evens
    del odds; del evens
    
    for p in players:
        img_elem = p.xpath(queries['img_elem'])[0]
        img_url = img_elem.get('src')
        name = img_elem.get('alt')
        p = Player(img_url, name)
        print p.name

    click_elem = \
        driver.find_element_by_xpath(click_elem_path(next_page))
    click_elem.click()