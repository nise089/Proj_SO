
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    age = models.IntegerField(label='Wie alt sind Sie?', max=125, min=18)
    gender = models.StringField(choices=[['female', 'weiblich'], ['male', 'männlich'], ['divers ', 'divers '], ['na', 'möchte keine Angaben machen']], label='Welchem Geschlecht ordnen Sie sich zu? ')
    job = models.StringField(choices=[['ja', 'ja'], ['nein', 'nein'], ['möchte keine Angaben machen', 'möchte keine Angaben machen']], label='Arbeiten Sie neben dem Studium in einer bezahlten (Neben-)Tätgkeit? ')
    trust_general = models.StringField(choices=[['1', 'Man kann den meisten Menschen vertrauen'], ['0', 'Man kann nicht vorsichtig genug sein']], label='Würden Sie ganz allgemein sagen, dass man den meisten Menschen vertrauen kann, oder dass man im Umgang mit Menschen nicht vorsichtig genug sein kann?', widget=widgets.RadioSelectHorizontal)
    pos_reciprocity = models.IntegerField(choices=[[0, '0 - beschreibt mich überhaupt nicht'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 -beschreibt mich perfekt']], label='Wenn mir jemand einen Gefallen tut, bin ich bereit ihn zu erwidern.')
    neg_reciprocity = models.IntegerField(choices=[[0, '0 - beschreibt mich überhaupt nicht'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 -beschreibt mich perfekt']], label='Wenn ich sehr ungerecht behandelt werde, räche ich mich bei der ersten Gelegenheit, selbst wenn Kosten entstehen, um das zu tun.')
    trade = models.IntegerField(choices=[[0, 'Für Ausweitung'], [1, 'Gegen Ausweitung']], label='Heutzutage spielt der internationale Handel eine wichtige Rolle in der EU: Das heißt, dass einerseits Waren und Dienstleistungen von außerhalb in die EU importiert und andererseits Waren und Dienstleistungen in die ganze Welt exportiert werden. Sind Sie für oder gegen eine Ausweitung des Handels der EU mit anderen Nationen?')
    priority_climat = models.IntegerField(choices=[[1, 'Dem Umweltschutz sollte Vorrang eingeräumt werden, auch wenn dadurch das Wirtschaftswachstum sinkt und Arbeitsplätze verloren gehen.'], [2, 'Dem Wirtschaftswachstum und der Schaffung von Arbeitsplätzen sollte Vorrang eingeräumt werden, selbst wenn darunter die Umwelt etwas leidet.']], label='Hier sind zwei Aussagen, die man hört, wenn über Umweltschutz und Wirtschaftswachstum geredet wird. Welche dieser beiden Aussagen kommt Ihrer eigenen Meinung am nächsten?')
    climate_importance = models.IntegerField(choices=[[1, 'außerst wichtig'], [2, 'sehr wichtig'], [3, 'mäßig wichtig'], [4, 'nicht so wichtig'], [5, 'überhaupt nicht wichtig']], label='Wie wichtig ist das Thema der globalen Erwärmung für Sie persönlich?')
    climate_worry = models.IntegerField(choices=[[1, 'sehr beunruhigt'], [2, 'ein wenig beunruhigt'], [3, 'nicht sehr beunruhigt'], [4, 'nicht im Geringsten beunruhigt']], label='Wie besorgt sind Sie über die globale Erwärmung?')
    climate_per_damage = models.IntegerField(choices=[[1, 'sehr viel'], [2, 'mäßig viel'], [3, 'nur wenig'], [4, 'überhaupt nicht'], [5, 'weiß ich nicht']], label='Wie sehr glauben Sie, dass die globale Erwärmung Ihnen persönlich schaden wird?')
    climate_future_damage = models.IntegerField(choices=[[1, 'sehr viel'], [2, 'mäßig viel'], [3, 'nur wenig'], [4, 'überhaupt nicht'], [5, 'weiß ich nicht']], label='Wie sehr wird die globale Erwärmung Ihrer Meinung nach künftigen Generationen von Menschen schaden?')
    climate_belief = models.IntegerField(choices=[[1, 'nur durch natürliche Prozesse '], [2, 'vor allem durch natürliche Prozesse '], [3, 'zu etwa gleichen Teilen durch natürliche Prozesse und menschliches Handeln '], [4, 'vor allem durch menschliches Handeln'], [5, 'nur durch menschliches Handeln'], [6, 'ich denke nicht, dass ein Klimawandel stattfindet']], label='Denken Sie, dass der Klimawandel durch natürliche Prozesse, durch menschliches Handeln oder durch beides verursacht wird?')
    energyredu_effect = models.IntegerField(choices=[[0, '0 - überhaupt nicht wahrscheinlich'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 - äußerst wahrscheinlich']], label='Stellen Sie sich jetzt vor, dass eine große Anzahl von Menschen ihren Energieverbrauch einschränken würde. Wie wahrscheinlich ist es Ihrer Meinung nach, dass man so den Klimawandel reduzieren könnte? ')
    energyredu_action = models.IntegerField(choices=[[0, '0 - überhaupt nicht wahrscheinlich'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 - äußerst wahrscheinlich']], label='Wie wahrscheinlich ist es Ihrer Meinung nach, dass sehr viele Menschen ihren Energieverbrauch tatsächlich einschränken im Versuch, den Klimawandel zu reduzieren?')
    energyredu_regulation = models.IntegerField(choices=[[0, '0 - überhaupt nicht wahrscheinlich'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 - äußerst wahrscheinlich']], label='Und wie wahrscheinlich ist es Ihrer Meinung nach, dass genug Staaten Maßnahmen ergreifen, um den Klimawandel zu reduzieren?')
    my_field = models.IntegerField()
    support_tax = models.IntegerField(choices=[[1, '1 - sehr dafür'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - sehr dagegen']], label='Erhöhung der Abgaben auf fossile Brennstoffe wie Öl, Gas und Kohle.')
    support_ban = models.IntegerField(choices=[[1, '1 - sehr dafür'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - sehr dagegen']], label='Ein gesetzliches Verbot für den Verkauf von Haushaltsgeräten mit der schlechtesten Energieeffizienz.')
    member_political = models.BooleanField(blank=True, initial=False)
    member_ecological = models.BooleanField(blank=True, initial=False)
    member_welfare = models.BooleanField(blank=True, initial=False)
    member_sports = models.BooleanField(blank=True, initial=False)
    member_other = models.BooleanField(blank=True, initial=False)
    info_newspaper = models.BooleanField(blank=True, initial=False)
    info_tv = models.BooleanField(blank=True, initial=False)
    info_radio = models.BooleanField(blank=True, initial=False)
    info_web = models.BooleanField(blank=True, initial=False)
    info_socialmedia = models.BooleanField(blank=True, initial=False)
    info_people = models.BooleanField(blank=True, initial=False)
    trust_press = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label=' Presse und das Zeitungswesen', widget=widgets.RadioSelectHorizontal)
    trust_tv = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label='Fernsehsender', widget=widgets.RadioSelectHorizontal)
    trust_unions = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label='Gewerkschaften', widget=widgets.RadioSelectHorizontal)
    trust_elections = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label='Wahlen', widget=widgets.RadioSelectHorizontal)
    trust_companies = models.StringField(choices=[['1', '1 - sehr viel Vertrauen'], ['2', '2'], ['3', '3'], ['4', '4 - überhaupt kein Vertrauen']], label=' Große Wirtschaftsunternehmen', widget=widgets.RadioSelectHorizontal)
    trust_banks = models.StringField(choices=[['1', '1 - sehr viel Vertrauen'], ['2', '2'], ['3', '3'], ['4', '4 - überhaupt kein Vertrauen']], label='Banken', widget=widgets.RadioSelectHorizontal)
    trust_envNGOs = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label='Umweltschutzorganisationen', widget=widgets.RadioSelectHorizontal)
    trust_welfareNGOs = models.StringField(choices=[['1', '1 - sehr viel Vertrauen'], ['2', '2'], ['3', '3'], ['4', '4 - überhaupt kein Vertrauen']], label=' Wohltätige oder humanitäre Organisationen', widget=widgets.RadioSelectHorizontal)
    trust_EU = models.StringField(choices=[['1', '1 - sehr viel Vertrauen'], ['2', '2'], ['3', '3'], ['4', '4 - überhaupt kein Vertrauen']], label='Europäische Union (EU)', widget=widgets.RadioSelectHorizontal)
    trust_UNO = models.IntegerField(choices=[[1, '1 - sehr viel Vertrauen'], [2, '2'], [3, '3'], [4, '4 - überhaupt kein Vertrauen']], label=' Vereinte Nationen (UNO)', widget=widgets.RadioSelectHorizontal)
    trust_universities = models.StringField(choices=[['1', '1 - sehr viel Vertrauen'], ['2', '2'], ['3', '3'], ['4', '4 - überhaupt kein Vertrauen']], label='Universitäten', widget=widgets.RadioSelectHorizontal)
    political_interest = models.IntegerField(choices=[[1, '1 - sehr interessiert'], [2, '2 - etwas interessiert'], [3, '3 - kaum interessiert'], [4, '4 - überhaupt nicht interessiert']], label='Wie stark interessieren Sie sich für Politik?')
    party_elect = models.IntegerField(choices=[[1, 'CDU/CSU'], [2, 'SPD'], [3, 'FDP'], [4, 'Bündnis 90/Die Grünen'], [5, 'Die Linke'], [6, 'AfD'], [7, 'andere'], [8, 'möchte keine Angabe machen']], label='Wenn morgen Bundestagswahl wäre, welche Partei würden Sie dann wählen?')
    measures_shower = models.BooleanField(blank=True, initial=False)
    measures_flights = models.BooleanField(blank=True, initial=False)
    measures_living = models.BooleanField(blank=True, initial=False)
    measures_nutrition = models.BooleanField(blank=True, initial=False)
    measures_electricity = models.BooleanField(blank=True, initial=False)
    measures_car = models.BooleanField(blank=True, initial=False)
    measures_consumption = models.BooleanField(blank=True, initial=False)
    measures_nothing = models.BooleanField(blank=True, initial=False)
class Intro(Page):
    form_model = 'player'
class Q1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'job', 'trust_general', 'pos_reciprocity', 'neg_reciprocity']
class Q2(Page):
    form_model = 'player'
    form_fields = ['trust_press', 'trust_tv', 'trust_unions', 'trust_universities', 'trust_elections', 'trust_companies', 'trust_banks', 'trust_envNGOs', 'trust_welfareNGOs', 'trust_EU', 'trust_UNO', 'political_interest', 'party_elect']
class Q3(Page):
    form_model = 'player'
    form_fields = ['member_political', 'member_ecological', 'member_welfare', 'member_sports', 'member_other', 'info_newspaper', 'info_tv', 'info_radio', 'info_web', 'info_socialmedia', 'info_people']
class Q4(Page):
    form_model = 'player'
    form_fields = ['energyredu_effect', 'energyredu_action', 'energyredu_regulation', 'climate_importance', 'climate_worry', 'climate_per_damage', 'climate_future_damage', 'climate_belief', 'support_tax', 'support_ban']
class Q5(Page):
    form_model = 'player'
    form_fields = ['measures_shower', 'measures_flights', 'measures_living', 'measures_nutrition', 'measures_electricity', 'measures_car', 'measures_consumption', 'measures_nothing', 'priority_climat', 'trade']
page_sequence = [Intro, Q1, Q2, Q3, Q4, Q5]