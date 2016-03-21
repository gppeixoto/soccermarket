import time
import numpy as np
import lxml.html
from selenium import webdriver
from consts import *
from utils import *
import pandas as pd

class Transfer:
    def __init__(self, name, img_url, position, value, age, season):
        self.name = name
        self.img_url = img_url
        self.position = position
        self.value = value
        self.age = age
        self.season = season

    def __str__(self):
        return str(self.to_tuple())

    def to_tuple(self):
        return (self.name, self.img_url, self.position, self.value, self.age, self.season)

    def get_params_names(self):
        return ['name', 'img_url', 'position', 'value', 'age', 'season']

driver = webdriver.Firefox()
driver.get(SEED_URL)
global_transfers = []
DEBUG = True

for next_page in xrange(2, 3):
    cur = 0
    time.sleep(30)
    source = driver.page_source
    tree = lxml.html.fromstring(source)
    
    odds = tree.xpath(queries['odds'])
    evens = tree.xpath(queries['evens'])
    transfers = odds+evens

    positions = get_positions(transfers, queries)
    values = get_market_values(transfers, queries)
    ages, seasons = get_age_season(transfers, queries)

    del odds; del evens;
    
    for t in transfers:
        img_elem = t.xpath(queries['img_elem'])[0]
        name = img_elem.get('alt')
        img_url = img_elem.get('src')
        pos = positions[cur]
        age = ages[cur]
        season = seasons[cur]
        value = values[cur]
        t = Transfer(name, img_url, pos, value, age, season)
        global_transfers.append(t)
        cur += 1

    if DEBUG:
        df = pd.DataFrame([trf.to_tuple() for trf in global_transfers], columns = global_transfers[0].get_params_names())
        print df.head(n=10)
    # click_elem = \
    #     driver.find_element_by_xpath(click_elem_path(next_page))
    # click_elem.click()  