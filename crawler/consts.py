SEED_URL = 'http://www.transfermarkt.co.uk/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=&plus=1'
PLAYER_SEEDS = "http://www.transfermarkt.co.uk/premier-league/marktwertaenderungen/wettbewerb/GB1/pos//detailpos/0/plus/1"
MANAGERS_SEED = "http://www.transfermarkt.de/trainer/verfuegbaretrainer/statistik?statistik=&plus=2&page="
MANAGERS_PREFIX = "http://www.transfermarkt.co.uk"
TEAMS_SEED = "http://www.transfermarkt.com/spieler-statistik/wertvollstemannschaften/marktwertetop?page="

USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'"
HEADERS = {'User-Agent': USER_AGENT}
LAST_PAGE = 10

queries = {
    "odds": "//tr[@class = 'odd']",
    "evens": "//tr[@class = 'even']",
    "img_elem" : 'td[@class=""]//img[@class="bilderrahmen-fixed"]',
    "positions" : '//td/table/tbody/tr/td',
    "market_values": '//td[@class = "rechts"]/text()',
    "age_season" : '//td[@class="zentriert"]//text()',
    "involved_teams": '//a[@class = "vereinprofil_tooltip"]',
    "transfer_values": '//td[@class = "rechts hauptlink"]/a/text()',
    "win_percentage": '//span[contains(text(), "Wins")]'
}
