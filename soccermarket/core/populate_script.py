import cPickle as pickle
import imp
import sys
from os import path
import models

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../crawler')))

from team_info_parser import Team
from manager_info_parser import Manager
from player_info_parser import Transfer, Player

data_path = "../data/"

def parse_win_percentage(win_percentage):
    if not win_percentage:
        return -1.0
    elif len(win_percentage) >= 4:
        num = win_percentage[:4]
        return float(num)
    else:
        return -1.0

def parse_age(age):
    if not age:
        return -1.0
    elif len(age) == 2:
        return float(age)
    else:
        return -1.0

def populate_teams():
    for i in xrange(100):
        filename = data_path + "team" + str(i) + ".p"
        with open(filename, "r") as file:
            team = pickle.load(file)
            team.name = team.full_name
            models.Team.objects.update_or_create(name = team.name, full_name = team.full_name, country = team.country, badge = team.badge, kit_image = team.kit_image)
            print "Team " + repr(team.name) + " was added to the database"
            populate_manager(team)

def populate_manager(team):
    manager = team.manager
    if manager is not None:
        win_percentage = parse_win_percentage(manager.win_percentage)
        age = parse_age(manager.age)
        name = manager.name.title()
        models.Coach.objects.update_or_create(name = name, age = age, nationality = manager.nationality, preferred_formation = manager.preferred_formation, win_percentage = win_percentage)
        print "Coach " + repr(name) + " was added to the database"
        bd_team = models.Team.objects.get(name = team.name)
        bd_coach = models.Coach.objects.get(name = name)
        models.Coaches.objects.update_or_create(coach = bd_coach, team = bd_team)

def populate():
    populate_teams()
    print "BD was populated successfully"
