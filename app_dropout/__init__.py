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


class GamePage(Page):
    # specific page class on which timeouts need to be checked; inherits all features of the Page class

    @staticmethod
    def is_displayed(player: Player):
        # show page only for players the group variable "has_dropout" is False == no dropout in group
        group = player.group
        return group.has_dropout is False

    @staticmethod
    def before_next_page(player:Player, timeout_happened):
        group = player.group
        # check if timeout happened
        if timeout_happened:
            group.has_dropout = True  # indicate that dropout happened in group
            player.is_dropout = True  # indicate that player dropped out


class Game(GamePage):
    timeout_seconds = 10


class Game2(GamePage):

    pass


class WaitForOthers(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout is False
    pass


class Dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.is_dropout

    pass


class DropoutVictim(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout and player.is_dropout is False

    pass


page_sequence = [Game, Game2, WaitForOthers, Dropout, DropoutVictim]
