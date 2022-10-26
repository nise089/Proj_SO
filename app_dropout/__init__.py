from otree.api import *

doc = """
Dropout detection for multiplayer game (end the game) 
"""


class C(BaseConstants):
    NAME_IN_URL = 'dropout_end_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_dropout = models.BooleanField(initial=False)


class Player(BasePlayer):
    is_dropout = models.BooleanField(initial=False)


class Game(Page):
    timeout_seconds = 10

    @staticmethod
    # check if timeout happened
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        if timeout_happened:
            group.has_dropout = True  # indicate that dropout happened in group
            player.is_dropout = True  # indicate that player dropped out


class Game2(Page):

    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout == False

    pass


class WaitForOthers(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout == False
    pass


class DropoutHappened(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        group = player.group
        if group.has_dropout:
            return upcoming_apps[-1]

    pass


page_sequence = [Game, Game2, WaitForOthers, DropoutHappened]
