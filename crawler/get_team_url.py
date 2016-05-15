import consts
import lxml.html
import requests

if __name__ == "__main__":
    with open("../data/teamsUrls.txt", "w") as outfile:
        for i in xrange(1, 5):
            url = consts.TEAMS_SEED + str(i)
            tree = lxml.html.fromstring(requests.get(url, headers=consts.HEADERS).text)
            result = tree.xpath('//a[@class = "vereinprofil_tooltip"]')
            for i, elem in enumerate(result):
                if i % 2 == 0:
                    href = elem.get('href')
                    print href
                    outfile.write(href+'\n')
