from otree.api import *

import random
import settings

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'decision_stage'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    profit = models.IntegerField(initial=130)  # TODO later profits from slider task

    profit_choice = models.StringField(
        widget=widgets.RadioSelect,
        label='Please choose how the profit should be used.',
        choices=['owner bonus', 'worker bonus', 'donation']
    )

    accepted_price = models.IntegerField(
        min=0,
        max=100,  # TODO adjust accr. calibration
        label='Your price offer:'
    )

    offered_price = models.IntegerField(min=0, max=100)

    sold = models.BooleanField(initial=False)
    pass


# PAGES
class ProfitChoice(Page):
    form_model = 'player'
    form_fields = ['profit_choice']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # applies only for investors for now
        if player.profit_choice == 'owner bonus':
            player.payoff = player.profit + settings.SESSION_CONFIG_DEFAULTS['dividend']
        else:
            player.payoff = settings.SESSION_CONFIG_DEFAULTS['dividend']
    pass


class SellingChoice(Page):
    form_model = 'player'
    form_fields = ['accepted_price']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # applies only for owners of MARKET companies for now
        # draw random offered price
        player.offered_price = random.randint(0, 100)
        # check if offered price >= accepted price
        # if true, switch sold to true
        if player.offered_price >= player.accepted_price:
            player.sold = True
            player.payoff += player.offered_price
        else:
            player.sold = False
    pass


class Results(Page):
    pass


page_sequence = [ProfitChoice, SellingChoice, Results]
