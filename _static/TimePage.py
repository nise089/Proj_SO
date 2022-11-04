from otree.api import *
from otree.app_template.models import Player


class TimePage(Page):
    # specific page class on which timeouts need to be checked; inherits all features of the Page class

    @staticmethod
    def is_displayed(player: Player):
        # show page only for players the group variable "has_dropout" is False == no dropout in group
        group = player.group
        return group.has_dropout is False

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        # check if timeout happened
        if timeout_happened:
            group.has_dropout = True  # indicate that dropout happened in group
            player.is_dropout = True  # indicate that player dropped out
