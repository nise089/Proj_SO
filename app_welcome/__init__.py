import csv
from itertools import cycle

from otree.api import *

c = cu

author = 'Denise Feigl'

doc = """
app_welcome App. 
Introduces the researcher and the experiment to the participants.
As for consent and move further to following app only if consent is given.
"""


def creating_session(subsession):
    print('Inside session method')
    # cycle over the order of company sizes until max number of participants is reached
    company_size_inter = cycle(C.order_of_company_sizes)
    # loop over participants and assign each participant to the next company size according to company_size_inter
    for player in subsession.get_players():
        # set treatment for specific player
        player.company_size = next(company_size_inter)
        print('participant', player.id_in_group, 'has company size', player.company_size)


class C(BaseConstants):
    NAME_IN_URL = 'app_welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    order_of_company_sizes = []
    csvFile_path = 'randomization_companysize.csv'
    csvFile = csv.reader(open(csvFile_path, encoding='utf-8'))
    for row in csvFile:
        print('csvFile row:', row)
        order_of_company_sizes.append(row[0])
        print('the order of company sizes:', order_of_company_sizes)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(initial=False)
    company_size = models.StringField()


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']


class Welcome(Page):
    form_model = 'player'

    def vars_for_template(self):
        return dict(participation_fee=self.session.config['participation_fee'])

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.company_size == "3members":
            return "app_founding_phase2"
        else:
            return "app_founding_phase"


page_sequence = [Consent, Welcome]
