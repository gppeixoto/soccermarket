SEED_URL = 'http://www.transfermarkt.co.uk/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1'

queries = {
    "odds": "//tr[@class = 'odd']",
    "evens": "//tr[@class = 'even']",
    "img_elem" : 'td[@class=""]//img[@class="bilderrahmen-fixed"]'
}

def click_elem_path(nb):
    return '//li[@class="page"]/a[text()==%d]' % nb