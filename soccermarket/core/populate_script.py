import cPickle as pickle
import imp
import sys
from os import path
import models
from datetime import datetime

sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../crawler')))

import consts
from team_info_parser import Team
from utils import get_team_id_from_url_populate as get_id

data_path = "../data/"

team_ids = {}

def parse_win_percentage(win_percentage):
    if not win_percentage:
        return -1.0
    elif len(win_percentage) >= 4:
        num = win_percentage[:4]
        try:
            return float(num)
        except ValueError:
            return -1.0
    else:
        return -1.0

def parse_number(num):
    if not num:
        return -1
    elif len(num) == 2:
        try:
            return int(num)
        except ValueError:
            return -1
    else:
        return -1

def parse_position(position):
    position_dict = {'Goalkeeper': 'GK','Defence - Centre Back': 'CB', 'Defence - Left-Back': 'LB', 'Defence - Right-Back': 'RB', 'Midfield - Defensive Midfield': 'DM', 
                     'Midfield - Central Midfield': 'CM', 'Midfield - Attacking Midfield': 'AM', 'Striker - Left Wing': 'LM', 'Striker - Right Wing': 'RM', 'Striker - Centre Forward': 'CF',
                     'Midfield - Left Wing': 'LM', 'Midfield - Right Wing': 'RM', 'Striker - Secondary Striker': 'CF', 'Midfield - Left Midfield' : 'LM', 'Midfield - Right Midfield' : 'RM'
                     }
    try:
        return position_dict[position]
    except KeyError:
        print position

def parse_market_value(market_value):
    value = market_value[:-1]
    try:
        return float(value)
    except ValueError:
        return -1.0

def parse_foot(foot):
    if foot == 'left':
        return 'L'
    else:
        return 'R'

def parse_team(team_id):
    try:
        name = team_ids[team_id]
        return models.Team.objects.get(name = name)
    except Exception:
        return None

def parse_date(date):
    try:
        return datetime.strptime(date, '%b %d, %Y').date()
    except Exception:
        print date

def populate_teams():
    for i in xrange(100):
        filename = data_path + "team" + str(i) + ".p"
        with open(filename, "r") as file:
            team = pickle.load(file)
            team.name = team.full_name
            team_ids[get_id(team.url_profile)] = team.name
            models.Team.objects.update_or_create(name = team.name, full_name = team.full_name, country = team.country, badge = team.badge)
            print "Team " + repr(team.name) + " was added to the database"
            populate_manager(team)
            populate_players(team)

def populate_manager(team):
    manager = team.manager
    if manager is not None:
        win_percentage = parse_win_percentage(manager.win_percentage)
        age = parse_number(manager.age)
        name = manager.name.title()
        models.Coach.objects.update_or_create(name = name, age = age, nationality = manager.nationality, preferred_formation = manager.preferred_formation, win_percentage = win_percentage)
        # print "Coach " + repr(name) + " was added to the database"
        bd_team = models.Team.objects.get(name = team.name)
        bd_coach = models.Coach.objects.get(name = name)
        models.Coaches.objects.update_or_create(coach = bd_coach, team = bd_team)

def populate_players(team):
    players = team.players
    print "Players " + str(len(players)) + " was added to the database"
    for player in players:
        age = parse_number(player.age)
        position = parse_position(player.position)
        value = parse_market_value(player.market_value)
        shirt_number = parse_number(player.age)
        foot = parse_foot(player.foot)

        if player.name == '':
            continue

        models.Player.objects.update_or_create(name = player.name, age = age, nationality = player.nationality, position = position, 
            market_value = value, dominant_foot = foot, shirt_number = shirt_number, agent = player.agent, url_profile = player.url_profile, picture = player.image_url)
        # print "Player " + repr(player.name) + " was added to the database"

        populate_transfers(player)

        bd_team = models.Team.objects.get(name = team.name)
        bd_player = models.Player.objects.get(name = player.name)
        models.Plays.objects.update_or_create(player = bd_player, team = bd_team)

def populate_transfers(player):
    transfer_history = player.transfer_history
    for transfer in transfer_history:
        origin = parse_team(transfer.origin_id)
        destination = parse_team(transfer.dest_id)
        value = parse_market_value(transfer.value)
        date = parse_date(transfer.date)
        if destination is not None and origin is not None:
            bd_player = models.Player.objects.get(name = player.name)
            models.Transfer.objects.create(player = bd_player, destiny = destination, origin = origin, value = value, date = date)

def clear_bd():
    models.Player.objects.all().delete()
    models.Coach.objects.all().delete()
    models.Team.objects.all().delete()

def populate():
    clear_bd()
    populate_teams()
    print "BD was populated successfully"