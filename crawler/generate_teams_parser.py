import team_info_parser
from team_info_parser import Team

if __name__ == "__main__":
    with open("../data/teams.csv", "w") as outfile:
        with open("../data/teamsUrls.csv", "r") as infile:
            for i, line in enumerate(infile):
                nextUrl = "http://www.transfermarkt.co.uk/" + line.strip()
                print nextUrl
                currentTeam = Team(nextUrl)
                try:
                    currentTeam.parse_info()
                    outfile.write(currentTeam.to_csv()+"\n")
                    print "\tparsed correctly team #%d" % i
                except Exception as e:
                    print "\tparsing error on team #%d" % i
                    print str(e)
