from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from models import Transfer, Plays, History

def remove_player(player, team):
    Plays.objects.get(player = player, team = team).delete()

def add_player(player, team):
    Plays.objects.create(player = player, team = team)

@receiver(pre_save, sender = Transfer)
def execute_transfer(sender, **kwargs):
    instance = kwargs.get('instance')
    old_team = instance.origin
    if old_team is not None:
        player = instance.player
        new_team = instance.destiny
        remove_player(player, old_team)
        add_player(player, new_team)

@receiver(post_save, sender = Plays)
def add_to_history(sender, created, instance, **kwargs):
    player = instance.player
    new_team = instance.team
    History.objects.create(player = player, team = new_team)
