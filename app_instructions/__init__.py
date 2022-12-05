from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_type_choice(label):
    return models.IntegerField(
        label= label,
        choices=[
            [1, "Company A"],
            [2, "Company B"],
            [3, "Company C"],
            [4, "Company D"]
        ],
    )


class Player(BasePlayer):
    control_working = models.IntegerField(
        label="The more sliders a worker solves, the higher…",
        choices=[
            [1, 'the profit'],
            [2, "the worker's payoff"],
            [3, "the owner’s payoff if s/he chooses the owner bonus in the profit choice after the same round"]
        ],
        widget=widgets.RadioSelect
    )

    control_profit_choice = models.IntegerField(
        label="Assume the profit choice is the worker bonus. Who receives a share of the profit?",
        choices=[
            [1, "Worker"],
            [2, "Owner, who is no worker"],
            [3, "Owner, who is also a worker"]
        ],
        widget=widgets.RadioSelect
    )

    control_selling_choice = models.IntegerField(
        label="In the selling choice, the company is sold if …",
        choices=[
            [1, "the computer’s offered price Z is higher than the owner’s selected price P."],
            [2, "the computer’s offered price Z is lower than the owner’s selected price P."],
            [3, "the owner chooses to sell the company"]
        ],
        widget=widgets.RadioSelect
    )

    control_types = models.IntegerField(
        label="The company types differ in ...",
        choices=[
            [1, "whether the owner is also a worker or not"],
            [2, "whether the owner can transfer the profit to him/herself by choosing the owner bonus"],
            [3, "the task the worker must complete"]
        ],
        widget=widgets.RadioSelect
    )

    company_choice_owner = make_type_choice(
        "Assume you were an owner and could choose which company type to found. /"
        "Which company would you prefer to found?"
    )

    company_choice_worker = make_type_choice(
        "Assume you were a (normal) worker and could choose for which company type you want to work. /"
        "In which company would you prefer to work?"
    )


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
    form_fields = ['control_working', 'control_profit_choice', 'control_selling_choice', 'control_types']


class CompanyChoiceOwner(Page):
    form_model = 'player'
    form_fields = ['company_choice_owner']


class CompanyChoiceWorker(Page):
    form_model = 'player'
    form_fields = ['company_choice_worker']


class Randomization(WaitPage):
    pass


page_sequence = [ControlQuestions, CompanyChoiceOwner, CompanyChoiceWorker]
