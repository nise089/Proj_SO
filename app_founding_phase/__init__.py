from otree.api import *


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
    pass


class Player(BasePlayer):
    founding = models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Do you want found the company?')
    pass


# PAGES
class FoundingChoice(Page):
    form_model = 'player'
    form_fields = ['founding']
    pass


class ResultsEnd(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.founding == False

    pass


page_sequence = [FoundingChoice, ResultsEnd]
