from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ObjectDoesNotExist
from models import Transfer, Plays, History

def add_history(player, team):
    try:
        History.objects.get(player = player, team = team)
    except ObjectDoesNotExist:
        History.objects.create(player = player, team = team)

def remove_player(player, team):
    try:
        Plays.objects.get(player = player, team = team).delete()
    except ObjectDoesNotExist: 
        print "Player already did not play for this team"
        add_history(player, team)

def add_player(player, team):
    try:
        Plays.objects.get(player = player, team = team)
    except ObjectDoesNotExist:
        try:
            Plays.objects.get(player = player).delete()
        except ObjectDoesNotExist:
            print "Player added to new team"
        Plays.objects.create(player = player, team = team)

@receiver(pre_save, sender = Transfer)
def execute_transfer(sender, **kwargs):
    instance = kwargs.get('instance')
    old_team = instance.origin
    player = instance.player
    new_team = instance.destiny
    if old_team is not None:
        remove_player(player, old_team)
    add_player(player, new_team)

@receiver(post_save, sender = Plays)
def add_to_history(sender, created, instance, **kwargs):
    player = instance.player
    new_team = instance.team
    add_history(player, new_team)
