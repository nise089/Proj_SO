
from otree.api import *
c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'app_feedback'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Intro(Page):
    pass


page_sequence = [Intro]
