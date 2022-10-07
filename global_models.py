from otree.api import *
from otree import settings

author = 'Denise Huber'

doc = """
Defining constants and methods that are consistent throughout the experiment
"""


class GlobalC(BaseConstants):
    wage = 0.2  # TODO set number from calibration
    payment_per_slider = 1  # TODO set number from calibration
    productivity = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class GlobalPlayer(BasePlayer):
    pass