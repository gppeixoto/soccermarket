SEED_URL = 'http://www.transfermarkt.co.uk/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1'

queries = {
    "odds": "//tr[@class = 'odd']",
    "evens": "//tr[@class = 'even']",
    "img_elem" : 'td[@class=""]//img[@class="bilderrahmen-fixed"]',
    "positions" : '//td/table/tbody/tr/td',
    "market_values": '//td[@class = "rechts"]/text()',
    "age_season" : '//td[@class="zentriert"]//text()',
    "involved_teams": '//a[@class = "vereinprofil_tooltip"]'
}