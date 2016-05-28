import team_info_parser
import consts
from player_info_parser import Player
from team_info_parser import Team
import cPickle as pickle

def main():
    with open("../data/teamsUrls.csv", "r") as infile:
        for i, line in enumerate(infile):
            team_url = consts.PREFIX + line.strip()
            print "Parsing team %s" % team_url
            current_team = Team(team_url)
            try:
                current_team.parse_info()
                num_players = 0
                for player in current_team.players_urls:
                    current_player = Player(consts.PREFIX + player)
                    try:
                        current_player.parse_info()
                        setattr(current_player, "tree", None)
                        current_team.players.append(current_player)
                        num_players += 1
                        print "\tparsed player %s" % player
                    except Exception as e:
                        print "\tparsing error on %s" % player
                print "\nparsed %d players" % num_players
                setattr(current_team, "tree", None)
                with open("team%d.p" % i, "w") as teamfile:
                    pickle.dump(current_team, teamfile)
            except Exception as e:
                print "\tparsing error on team #%d" % i
            finally:
                print
                print "#"*40
                print

if __name__ == '__main__':
    main()