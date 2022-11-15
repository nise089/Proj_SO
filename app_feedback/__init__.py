
from otree.api import *
c = cu

doc = 'App for debriefing and feedback survey'


class C(BaseConstants):
    NAME_IN_URL = 'app_feedback'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


def make_choice(label):
    return models.IntegerField(
        label=label,
        choices=[
            [1, 'strongly disagree'],
            [2, 'somewhat disagree'],
            [3, 'neither agree nor disagree'],
            [4, 'somewhat agree'],
            [5, 'strongly agree']
        ]
    )


def make_textfield(label):
    return models.LongStringField(
        label=label,
        blank=True
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_carefully = make_choice('I made my decisions carefully')

    attention_randomly = make_choice('I made the decisions in this study randomly')

    attention_understood = make_choice('I understood what my decisions meant for my payment')

    attention_left = make_choice('Please check the option on the far left')

    attention_right = make_choice('Please check the option on the far right')

    feedback_problems = make_textfield('Did you encounter any problems in the study?')

    feedback_typos = make_textfield('Did you see any typos?')

    feedback_other = make_textfield('Is there anything else you want to tell us?')

    feedback_clarity = models.IntegerField(
        label="On a scale from 0 'not clear at all' to 10 'perfectly clear'. How clear were the instructions to you?",
        max=0, min=10,
        widget=widgets.RadioSelectHorizontal
    )


class Intro(Page):
    pass


page_sequence = [Intro]
