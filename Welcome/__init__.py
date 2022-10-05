
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    consent = models.IntegerField(choices=[[1, 'Ja'], [0, 'Nein']], label='Ich kenne meine Rechte und bin mit der Teilnahme an dieser Studie einverstanden.', widget=widgets.RadioSelectHorizontal)
def consent_error_message(player: Player, value):
    if value == 0:
        return 'Bitte bestätigen Sie, dass Sie Ihre Rechte kennen und mit der Teilnahme an dieser Studie einverstanden sind'
class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']
class Info(Page):
    form_model = 'player'
class Next(Page):
    form_model = 'player'
page_sequence = [Welcome, Info, Next]