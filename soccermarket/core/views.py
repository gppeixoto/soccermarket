from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from models import *
from itertools import chain
from operator import attrgetter

# DEBUG
import logging
import os
logger = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Dangerous line of code below; will clear all people in the databae
Player.objects.all().delete()
Coach.objects.all().delete()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

player = Player(age='12', name='Asdolfo', nationality='Botsuana', position='GK', market_value='9', dominant_foot='R', shirt_number='9', agent='ackbar', url_profile='http://www.vini.com')
logger.info('PLAYER CREATED')

coach = Coach(age='2', name='Asdolfsky', nationality='Russia', preferred_formation='4-3-3', win_percentage='21')
logger.info('COACH CREATED')

player.save()
coach.save()

#################################

# Create your views here.
def index(request):
    return render(request, 'soccermarket.html')

def search_people(request): 
    logger.info('searching people')
    if request.method == 'POST':
        logger.info('POST OK')
        text = request.POST['search']
        players = Player.objects.filter(name__contains=text)
        coaches = Coach.objects.filter(name__contains=text)
        people_list = sorted(chain(players, coaches), key=attrgetter('name'))
        logger.info(len(people_list))
        for i in people_list:
            i.name = i.name.strip()
            logger.info(i.name)
        return render(request, 'soccermarket.html', { 'people': people_list })
        # users = Usuario.objects.filter(username__contains=text)
        # questoes = Questao.objects.filter(nome__contains=text)
        # for i in questoes:
        #     i.nome = i.nome.strip()
        # return render(request, 'search/search.html', { 'users' : users , 'questoes' : questoes[:100] })
    return redirect(reverse('index'))
