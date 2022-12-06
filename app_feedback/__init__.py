
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
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
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
        label="On a scale from 0 'not clear at all' to 10 'perfectly clear', how clear were the instructions to you?",
        choices=[1, 2, 3, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )


class Part3(Page):
    pass


class Q1(Page):
    form_model = 'player'
    form_fields = ['attention_randomly', 'attention_understood', 'attention_left', 'attention_right']


class Q2(Page):
    form_model = 'player'
    form_fields = ['feedback_problems', 'feedback_typos', 'feedback_clarity', 'feedback_other']


class Payment(Page):

    def vars_for_template(self):
        return dict(participation_fee=self.session.config['participation_fee'])


page_sequence = [Part3, Q1, Q2, Payment]
