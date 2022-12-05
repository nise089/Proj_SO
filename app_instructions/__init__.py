from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Part2(Page):
    pass


class LifeCycle(Page):
    pass


class Work(Page):
    pass


class ProfitChoice(Page):
    pass


class SellingChoice(Page):
    pass


class SummaryProduction(Page):
    pass


class Types(Page):
    pass


class OwnersRole(Page):
    pass


class DecisionSpace(Page):
    pass


class SummaryTypes(Page):
    pass


page_sequence = []
