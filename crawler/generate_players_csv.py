import player_info_parser
from player_info_parser import Player

if __name__ == "__main__":
    with open("../data/players.csv", "w") as outfile:
        with open("../data/playersUrls.csv", "r") as infile:
            for i, line in enumerate(infile):
                nextUrl = "http://www.transfermarkt.co.uk/" + line.strip()
                print nextUrl
                currentPlayer = Player(nextUrl)
                try:
                    currentPlayer.parse_info()
                    outfile.write(currentPlayer.to_csv()+"\n")
                    print "\tparsed correctly player #%d" % i
                except Exception as e:
                    print "\tparsing error on player #%d" % i
                    print str(e)
