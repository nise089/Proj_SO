from otree.api import *

from _static.TimePage import TimePage

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'founding_phase'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_dropout = models.BooleanField(initial=False)
    founding = models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Do you want to found the company?')


class Player(BasePlayer):
    is_dropout = models.BooleanField(initial=False)


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True


def set_group_id(group: Group):
    """ Stor Group ID of this subsession in a participant variable """
    for p in group.get_players():
        p.participant.group_id = group.id_in_subsession
        print(p.participant.group_id)


class RoleWaitPage(WaitPage):
    @staticmethod
    def assign_roles(group: Group):
        """ call set_group_id method and assign role (job) to each participant in the group """
        set_group_id(group)
        for p in group.get_players():
            if p.id_in_group == 1:
                p.participant.job = "owner"
            else:
                p.participant.job = "worker"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    after_all_players_arrive = assign_roles


class Role(Page):
    pass


class FoundingChoice(TimePage):
    timeout_seconds = 120
    form_model = 'group'
    form_fields = ['founding']

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.participant.job == "owner"


class FoundingWaitPage(WaitPage):
    pass


class ResultsEnd(TimePage):
    timeout_seconds = 120

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition


class Dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout


page_sequence = [GroupingWaitPage, RoleWaitPage, Role, FoundingChoice, FoundingWaitPage,  ResultsEnd, Dropout]
