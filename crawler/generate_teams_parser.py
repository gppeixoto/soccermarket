import team_info_parser
import consts
from player_info_parser import Player
from team_info_parser import Team
from manager_info_parser import Manager
import cPickle as pickle

def main():
    with open("../data/teamsUrls.csv", "r") as infile:
        for i, line in enumerate(infile):
            team_url = consts.PREFIX + line.strip()
            print "Parsing team %s" % team_url
            current_team = Team(team_url)
            try:
                current_team.parse_info()
                print "\tmanager_url: %s" % current_team.manager_url
                manager = Manager(consts.PREFIX + current_team.manager_url)
                manager.parse_info()
                setattr(manager, "tree", None)
                setattr(current_team, "manager", manager)
                print "\tparsed manager %s" % current_team.manager.name
                num_players = 0
                for player in current_team.players_urls:
                    current_player = Player(consts.PREFIX + player)
                    try:
                        current_player.parse_info()
                        print current_player.transfer_history
                        setattr(current_player, "tree", None)
                        current_team.players.append(current_player)
                        num_players += 1
                        print "\tparsed player %s" % current_player.name
                    except Exception as e:
                        print "\tparsing error on %s" % player
                        print str(e)
                print "\nparsed %d players" % num_players
                setattr(current_team, "tree", None)
                with open("../data/team%d.p" % i, "w") as teamfile:
                    pickle.dump(current_team, teamfile)
            except Exception as e:
                print "\tparsing error on team #%d" % i
                print str(e)
            finally:
                print
                print "#"*40
                print

if __name__ == '__main__':
    main()
