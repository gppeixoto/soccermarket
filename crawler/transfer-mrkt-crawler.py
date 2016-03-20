import time
import numpy as np
import lxml.html
from selenium import webdriver
from consts import *
from utils import *

class Transfer:
    def __init__(self, img_url, name, position):
        self.name = name
        self.img_url = img_url
        self.position = position

    def __str__(self):
        return str((self.name, self.img_url, self.position))

    def to_tuple(self):
        return (self.name, self.img_url, self.position)

driver = webdriver.Firefox()
driver.get(SEED_URL)
global_transfers = []
DEBUG = True

for next_page in xrange(2, 3):
    time.sleep(30)
    source = driver.page_source
    tree = lxml.html.fromstring(source)
    
    odds = tree.xpath(queries['odds'])
    evens = tree.xpath(queries['evens'])
    transfers = odds+evens    
    positions = get_positions(transfers, queries)

    cur = 0
    del odds; del evens
    
    for t in transfers:
        img_elem = t.xpath(queries['img_elem'])[0]
        name = img_elem.get('alt')
        img_url = img_elem.get('src')
        pos = positions[cur]
        t = Transfer(img_url, name, pos)
        if DEBUG:
            print t
        global_transfers.append(t)

        
    # click_elem = \
    #     driver.find_element_by_xpath(click_elem_path(next_page))
    # click_elem.click()  