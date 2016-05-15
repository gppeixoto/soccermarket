# http://www.transfermarkt.co.uk/walter-novellino/profil/trainer/515
# http://www.transfermarkt.de/trainer/verfuegbaretrainer/statistik?statistik=&plus=2&page=1

import consts
import lxml.html
import requests

if __name__ == "__main__":
    with open("../data/managersUrls.txt", "w") as outfile:
        for i in xrange(1, 21):
            url = consts.MANAGERS_SEED + str(i)
            tree = lxml.html.fromstring(requests.get(url, headers=consts.HEADERS).text)
            result = tree.xpath('//td[@class="hauptlink"]')
            for elem in result:
                href = elem.getchildren()[0].get('href')
                if "trainer" in href:
                    print href
                    outfile.write(href+'\n')
