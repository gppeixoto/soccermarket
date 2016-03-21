import time
import numpy as np
import lxml.html
from selenium import webdriver
from consts import *
from utils import *
import pandas as pd

class Transfer:
    def __init__(self, name, img_url, position, mkt_value, age, season, from_, to, transf_val):
        self.name = name
        self.img_url = img_url
        self.position = position
        self.mkt_value = value
        self.age = age
        self.season = season
        self.from_ = from_
        self.to = to
        self.transf_val = transf_val

    def __str__(self):
        return str(self.to_tuple())

    def to_tuple(self):
        return (self.name, self.img_url, self.position, self.mkt_value, self.age, self.season, self.from_, self.to, self.transf_val)

    def get_params_names(self):
        return ['name', 'img_url', 'position', \
                'mkt_value', 'age', 'season', 'from_', 'to', 'transf_val']

driver = webdriver.Firefox()
driver.get(SEED_URL)
global_transfers = []
DEBUG = True

for next_page in xrange(2, 4):
    cur = 0
    print "current page: %d" % (next_page-1)
    print "waiting 30s..."
    time.sleep(30)

    print "parsing source code"
    source = driver.page_source
    tree = lxml.html.fromstring(source)
    
    odds = tree.xpath(queries['odds'])
    evens = tree.xpath(queries['evens'])
    transfers = odds+evens

    print "parsing fields"
    positions = get_positions(transfers, queries)
    market_values = get_market_values(transfers, queries)
    ages, seasons = get_age_season(transfers, queries)
    from_, to = get_involved_teams(transfers, queries)
    transfer_values = get_transfer_values(transfers, queries)

    del odds; del evens;
    
    for t in transfers:
        img_elem = t.xpath(queries['img_elem'])[0]
        name = img_elem.get('alt')
        img_url = img_elem.get('src')
        pos = positions[cur]
        age = ages[cur]
        season = seasons[cur]
        mkt_value = market_values[cur]
        fr_ = from_[cur]
        to_ = to[cur]
        transf_val = transfer_values[cur]
        t = Transfer(name, img_url, pos, mkt_value, age, season, fr_, to_, transf_val)
        global_transfers.append(t)
        cur += 1

    click_elem = get_next_page(driver, next_page)
    click_elem.click()

if DEBUG:
    df = pd.DataFrame([trf.to_tuple() for trf in global_transfers], columns=global_transfers[0].get_params_names())
    print df.head(n=10)
    print len(df)