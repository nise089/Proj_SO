from otree.api import *


doc = """
App to ask understanding questions with multiple choice widget 
(Source: https://s3.amazonaws.com/otreehub/browsable_source/1e38462b-46c7-4ca1-bca5-536462f90131/multi_select/index.html )
and questions on company preference with list ranking widget
(Source: https://s3.amazonaws.com/otreehub/browsable_source/1e38462b-46c7-4ca1-bca5-536462f90131/rank_widget/index.html)
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_control_and_preferences'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = ['A', 'B', 'C', 'D']
    CONTROLS = [
        "profit", "worker_payoff", "owner_payoff",
        'profit_choice_worker', 'profit_choice_owner', 'profit_choice_stewardowner',
        'selling_choice_higher', 'selling_choice_lower', 'selling_choice_owner',
        'types_owner', 'types_decision', 'types_task'
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    profit = models.BooleanField(blank=True)
    worker_payoff = models.BooleanField(blank=True)
    owner_payoff = models.BooleanField(blank=True)

    profit_choice_owner = models.BooleanField(blank=True)
    profit_choice_worker = models.BooleanField(blank=True)
    profit_choice_stewardowner = models.BooleanField(blank=True)

    selling_choice_higher = models.BooleanField(blank=True)
    selling_choice_lower = models.BooleanField(blank=True)
    selling_choice_owner = models.BooleanField(blank=True)

    types_owner = models.BooleanField(blank=True)
    types_decision = models.BooleanField(blank=True)
    types_task = models.BooleanField(blank=True)

    company_ranking_owner = models.BooleanField(blank=True)
    company_ranking_worker = models.BooleanField(blank=True)


# PAGES
class ControlQuestions(Page):
    form_model = 'player'
    form_fields = C.CONTROLS

    def error_message(self, values):
        solutions = dict(
            profit=True,
            worker_payoff=True,
            owner_payoff=True,
            profit_choice_worker=True,
            profit_choice_owner=False,
            profit_choice_stewardowner=True,
            selling_choice_higher=True,
            selling_choice_lower=False,
            selling_choice_owner=False,
            types_owner=True,
            types_decision=True,
            types_task=True
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Your answer is wrong. Please try again'

        return error_messages


class CompanyChoiceOwner(Page):
    form_model = 'player'
    form_fields = ['company_ranking_owner']


class CompanyChoiceWorker(Page):
    form_model = 'player'
    form_fields = ['company_ranking_worker']


class Randomization(WaitPage):
    pass


page_sequence = [ControlQuestions, CompanyChoiceOwner, CompanyChoiceWorker]
