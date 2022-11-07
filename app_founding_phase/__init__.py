from otree.api import *

from _static.TimePage import TimePage

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'founding_phase'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_dropout = models.BooleanField(initial=False)


class Player(BasePlayer):
    founding = models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Do you want to found the company?')
    is_dropout = models.BooleanField(initial=False)


# PAGES
class FoundingChoice(TimePage):
    timeout_seconds = 10
    form_model = 'player'
    form_fields = ['founding']


class ResultsEnd(TimePage):
    timeout_seconds = 10

    @staticmethod
    def is_displayed(player: Player):
        return player.founding is False


class Dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout


page_sequence = [FoundingChoice, ResultsEnd, Dropout]
