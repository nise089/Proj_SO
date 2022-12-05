from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = ['A', 'B', 'C', 'D']
    MORE_SLIDERS = [
        'the profit',
        "the worker's payoff",
        "the owner’s payoff if s/he chooses the owner bonus in the profit choice after the same round"
    ]
    WORKER_BONUS = ["Worker", "Owner, who is no worker", "Owner, who is also a worker"]
    SELLING = [
        "the computer’s offered price Z is higher than the owner’s selected price P.",
        "the computer’s offered price Z is lower than the owner’s selected price P.",
        "the owner chooses to sell the company"
    ]
    TYPE = [
        "whether the owner is also a worker or not",
        "whether the owner can transfer the profit to him/herself by choosing the owner bonus",
        "the task the worker must complete"
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_control_models():
    return models.BooleanField(blank=True)


class Player(BasePlayer):
    control_working_profit = make_control_models()
    control_working_worker_payoff = make_control_models()
    control_working_owner_payoff = make_control_models()

    control_profit_choice_owner = make_control_models()
    control_profit_choice_worker = make_control_models()
    control_profit_choice_stewardowner = make_control_models()

    control_selling_choice_higher = make_control_models()
    control_selling_choice_lower = make_control_models()
    control_selling_choice_owner = make_control_models()

    control_types_owner = make_control_models()
    control_types_decision = make_control_models()
    control_types_task = make_control_models()

    company_ranking_owner = models.StringField()
    company_ranking_worker = models.StringField()


# PAGES
class Part2(Page):
    pass


class LifeCycle(Page):
    pass


class Work(Page):
    pass


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


class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['control_working_profit', 'control_working_worker_payoff', 'control_working_owner_payoff']


class CompanyChoiceOwner(Page):
    form_model = 'player'
    form_fields = ['company_ranking_owner']


class CompanyChoiceWorker(Page):
    form_model = 'player'
    form_fields = ['company_ranking_worker']


class Randomization(WaitPage):
    pass


page_sequence = [ControlQuestions]
