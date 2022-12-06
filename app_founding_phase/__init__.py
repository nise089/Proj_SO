from otree.api import *

from _static.Enums import CompanyTypesEnum, JobsEnum
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


class RoleWaitPage(WaitPage):
    @staticmethod
    def assign_roles_and_company_type(group: Group):
        """ call set_group_id method and assign role (job) to each participant in the group """
        for player in group.get_players():
            RoleWaitPage.set_group_id(player)
            RoleWaitPage.assign_role(player)
            RoleWaitPage.assign_company_type(player)

    @staticmethod
    def set_group_id(player: Player):
        """ Stor Group ID of this subsession in a participant variable """
        player.participant.group_id = player.group.id_in_subsession
        print(player.participant.group_id)

    @staticmethod
    def assign_role(player: Player):
        """ assign role to each player of one group """
        if player.id_in_group == 1:
            player.participant.job = JobsEnum.OWNER
        else:
            player.participant.job = JobsEnum.WORKER

    @staticmethod
    def assign_company_type(player: Player):
        """ assign company type to each player of the same group """
        if (player.participant.group_id % 2) == 0:
            player.participant.company_type = CompanyTypesEnum.FOUNDATION_OWNED
            print("company type is", player.participant.company_type.value)
        else:
            player.participant.company_type = CompanyTypesEnum.INVESTOR_OWNED
            print("company type is", player.participant.company_type)

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    after_all_players_arrive = assign_roles_and_company_type


class Role(Page):
    pass


class FoundingChoice(TimePage):
    timeout_seconds = 120
    form_model = 'group'
    form_fields = ['founding']

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.participant.job == JobsEnum.OWNER


class FoundingWaitPage(WaitPage):
    pass


class ResultsEnd(TimePage):
    timeout_seconds = 120

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and not player.group.founding

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return "app_feedback"


class Dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout


page_sequence = [GroupingWaitPage, RoleWaitPage, Role, FoundingChoice, FoundingWaitPage, ResultsEnd, Dropout]
