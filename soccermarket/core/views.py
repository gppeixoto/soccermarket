from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.db.models import Q
from models import *
from itertools import chain
from operator import attrgetter
import datetime

# DEBUG
import logging
import os
logger = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Dangerous line of code below; will clear everything in the database
# Player.objects.all().delete()
# Coach.objects.all().delete()
# Team.objects.all().delete();
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# player = Player(age='12', name='Asdolfo', nationality='Botsuana', position='GK', market_value='9', dominant_foot='R', shirt_number='9', agent='ackbar', url_profile='http://www.vini.com')
# logger.info('PLAYER CREATED')

# coach = Coach(age='2', name='Asdolfsky', nationality='Russia', preferred_formation='4-3-3', win_percentage='21')
# logger.info('COACH CREATED')

# team = Team(name='Timao', full_name="Timao e Pumba", country="Brazil", badge="http://www.vini.com", kit_image='http://www.vini.com')
# logger.info("TEAM CREATED")

# team2 = Team(name='Nautico', full_name="Clube Nautico Capibaribe", country="Brazil", badge="http://www.vini.com", kit_image='http://www.vini.com')
# logger.info("ANOHER TEAM CREATED")

# player.save()
# coach.save()
# team.save()
# team2.save();

#################################

# Create your views here.
def index(request):
    return render(request, 'soccermarket.html')

def team(request):
    if request.method == 'POST':
        logger.info('POST OK')
        name = request.POST['name']

        team = Team.objects.filter(
            Q(name__contains=name)
            )

        plays = Plays.objects.filter(
            Q(team__name__contains=name)
            )

        coaches = Coaches.objects.filter(
            Q(team__name__contains=name)
            )

        return render(request, 'team.html', { 'team': team, 'plays': plays, 'coaches': coaches })
    return render(request, 'team.html')

def player(request):
    if request.method == 'POST':
        logger.info('POST OK')
        name = request.POST['name']

        player = Player.objects.filter(
            Q(name__contains=name)
            )

        plays = Plays.objects.filter(
            Q(player__name__contains=name)
            )

        coach = Coach.objects.filter(
            Q(name__contains=name)
            )

        coaches = Coaches.objects.filter(
            Q(coach__name__contains=name)
            )

        history = History.objects.filter(
            Q(player__name__contains=name)
            )

        transfer = Transfer.objects.filter(
            Q(player__name__contains=name)
            )

        return render(request, 'player.html', { 'player': player, 'plays': plays, 'coach': coach, 'coaches': coaches, 'history': history, 'transfer': transfer })
    return render(request, 'player.html')
    
def transfer(request):
    if request.method == 'POST':
        logger.info('POST OK')
        name = request.POST['name']
        origin = request.POST['origin']
        destiny = request.POST['destiny']

        transfer = Transfer.objects.filter(
            Q(player__name__contains=name) & 
            Q(destiny__name__contains=destiny) &
            Q(origin__name__contains=origin)
            )

        return render(request, 'transfer.html', { 'transfer': [transfer[0]] })
    return render(request, 'transfer.html')

def search(request): 
    logger.info('searching all things')
    if request.method == 'POST':
        logger.info('POST OK')
        text = request.POST['search']

        # search people
        players = Player.objects.filter(
            Q(name__contains=text) |
            Q(nationality__contains=text)
            )

        coaches = Coach.objects.filter(
            Q(name__contains=text) |
            Q(nationality__contains=text)
            )

        # search teams
        teams = Team.objects.filter(
            Q(name__contains=text) | 
            Q(full_name__contains=text) |
            Q(country__contains=text)
            ).order_by('name')

        # search transfers
        transfers = Transfer.objects.filter(
            Q(player__name__contains=text) | 
            Q(destiny__name__contains=text) |
            Q(origin__name__contains=text)
            ).order_by('player__name')

        # people sorted by name
        people_list = sorted(chain(players, coaches), key=attrgetter('name'))

        logger.info(len(people_list))
        logger.info(teams.count())
        for i in people_list:
            i.name = i.name.strip()
            logger.info(i.name)
        for i in teams:
            logger.info(i.name)

        return render(request, 'search.html', { 'people': people_list, 
            'teams': teams, 'transfers': transfers })
    return redirect(reverse('index'))
