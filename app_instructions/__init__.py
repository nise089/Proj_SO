from otree.api import *
from otree import settings

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    EXCHANGE_RATE = settings.SESSION_CONFIG_DEFAULTS['real_world_currency_per_point']
    ENDOWMENT = settings.SESSION_CONFIG_DEFAULTS['E']
    WAGE = settings.SESSION_CONFIG_DEFAULTS['wage']
    PIECERATE = settings.SESSION_CONFIG_DEFAULTS['piecerate']
    PRODUCTIVITY = settings.SESSION_CONFIG_DEFAULTS['productivity']
    FIXED_REVENUE = settings.SESSION_CONFIG_DEFAULTS['Rfixed']
    DIVIDEND = settings.SESSION_CONFIG_DEFAULTS['dividend']
    N = settings.SESSION_CONFIG_DEFAULTS['n']
    ROUNDS = settings.SESSION_CONFIG_DEFAULTS['rounds']
    SLIDERTIME = settings.SESSION_CONFIG_DEFAULTS['max_slidertime']

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

    def vars_for_template(player: Player):
        return dict(
            cost_factor=C.DIVIDEND + C.N * C.WAGE,
            profit_factor=C.PRODUCTIVITY - C.PIECERATE,
            profit_fixed=C.FIXED_REVENUE - C.DIVIDEND - C.N * C.WAGE,
        )


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


page_sequence = [
    Part2, LifeCycle, Work, ProfitChoice, SellingChoice, SummaryProduction, Types, OwnersRole, DecisionSpace,
    SummaryTypes
]
