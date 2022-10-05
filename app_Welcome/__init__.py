
from otree.api import *
c = cu

author = 'Denise Feigl'

doc = """
app_Welcome App. 
Introduces the researcher and the experiment to the participants.
As for consent and move further to following app only if consent is given.
"""
class C(BaseConstants):
    NAME_IN_URL = 'app_Welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    consent = models.BooleanField()
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']
class Welcome(Page):
    form_model = 'player'
class Next(Page):
    form_model = 'player'

page_sequence = [Consent, Welcome, Next]