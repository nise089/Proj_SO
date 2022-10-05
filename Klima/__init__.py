
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Klima'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    import itertools
    pressures = itertools.cycle([True, False])
    for player in subsession.get_players():
        player.time_pressure = next(pressures)
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    prior_belief = models.IntegerField(choices=[[1, '1- überhaupt nicht zuversichtlich'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - sehr zuversichtlich']], label='Wie zuversichtlich sind Sie, dass die internationale Klimapolitik erfolgreich darin sein wird, den Anstieg der globalen Durchnittstemperatur gegenüber vorindustriellem Werten zu begrenzen und zu stabilisieren?')
    pn1 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Bislang haben sich 136 von 198 Ländern das Ziel gesetzt, ihre Emissionen auf Netto-Null zu reduzieren. Diese Länder sind zusammen für etwa 83% der weltweiten Emissionen verantwortlich, erzeugen 91% des weltweiten Bruttoinlandsprodukts (kaufkraftbereinigt) und umfassen 80% der weltenweiten Bevölkerung. ', widget=widgets.RadioSelectHorizontal)
    pn2 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Sowohl auf EU-Ebene als auch im US-Senat gab es im letzten Jahr Entwürfe für einen CO2-Grenzausgleich. Durch einen CO2-Grenzausgleich wird der CO2-Gehalt von Importen so besteuert, dass kein Anreiz für die Verlagerung energieintensiver Industrien ins Ausland entsteht. Zugleich soll ein CO2-Grenzausgleich als klimapolitischer Hebel dienen, um andere Staaten zur Kooperation in der Klimapolitik zu motivieren. ', widget=widgets.RadioSelectHorizontal)
    pn3 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Beim Klimagipfel in Glasgow 2021 haben sich mehr als 40 Länder im „Global Coal to Clean Power Transition-Statement" zum beschleunigten Ausstieg aus der Kohleverstromung sowie dem Verzicht auf neue Kohlekraftwerke bekannt. Darunter sind große Kohleverbraucher wie Kanada, Polen, Vietnam und Chile.', widget=widgets.RadioSelectHorizontal)
    pn4 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Weltweit arbeiten immer mehr Staaten, Regionen und Städte an Plänen zum Ende von neu zugelassenen Autos mit Verbrennungsmotoren. Darunter sind Industriestaaten wie das Vereinigte Königreich, Kanada, die USA und Südkorea aber auch Schwellen- und Entwicklungsländer wie China, Indien, Ägypten, Indonesien, Thailand, Ghana und Marokko. Auch das Europäische Parlament hat zuletzt für ein Ende des Verbrennungsmotors gestimmt.', widget=widgets.RadioSelectHorizontal)
    nn1 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='2021 war der CO2 Ausstoß so hoch wie nie zuvor. Gegenüber dem Vorjahr ergab sich ein Anstieg von mehr als zwei Milliarden Tonnen CO2. Gründe hierfür liegen vor allem in der weltweit verstärkten Nutzung von Kohle. Den größten Anteil an diesem Anstieg hat China mit 33% an den weltweiten Gesamtemissionen.', widget=widgets.RadioSelectHorizontal)
    nn2 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Weltweit belaufen sich die Subventionen für fossile Energieträger auf 5,9 Billionen Dollar. Das entspricht 6,8 Prozent des weltweiten Bruttoinlandsprodukts im Jahr 2020. Bis 2025 wird ein Anstieg dieser auf ca. 7,4 Prozent des weltweiten Bruttoinlandsprodukts erwartet.', widget=widgets.RadioSelectHorizontal)
    nn3 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Der Oberste Gerichtshof der USA hat die Biden-Regierung in ihren Befugnissen beim Kampf gegen den Klimawandel eingeschränkt. In seinem Urteil kam der Supreme Court zu dem Schluss, dass eine Behörde in Fragen von großer Bedeutung und gesellschaftlicher Tragweite nicht ohne ausdrückliche Genehmigung des Kongresses agieren kann. Konkret entschied der Supreme Court, dass die US-Umweltschutzagentur keine CO2-Grenzwerte für bestehende kohle- und gasbefeuerte Kraftwerke festlegen darf. ', widget=widgets.RadioSelectHorizontal)
    nn4 = models.IntegerField(choices=[[1, '1 - Sehr schlechte Nachricht'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Sehr gute Nachricht']], label='Für den Umstieg auf erneuerbare Energien werden große Mengen von Spezialrohstoffen wie seltene Erden, Lithium, Kobalt, Nickel und Kupfer benötigt. Viele dieser Rohstoffe sind bereits heute knapp und es gibt eine hohe weltweite Abhängigkeit von einzelnen Produzentenländern. Die Internationale Energieagentur warnt angesichts stark gestiegener Preise, dass kritische Mineralien einen jahrzehntelangen Trend hin zu sinkenden Kosten für erneuerbare Energien bedrohen würden.', widget=widgets.RadioSelectHorizontal)
    posterior_belief_15 = models.IntegerField(choices=[[0, '0%'], [1, '1%'], [2, '2%'], [3, '3%'], [4, '4%'], [5, '5%'], [6, '6%'], [7, '7%'], [8, '8%'], [9, '9%'], [10, '10%'], [11, '11%'], [12, '12%'], [13, '13%'], [14, '14%'], [15, '15%'], [16, '16%'], [17, '17%'], [18, '18%'], [19, '19%'], [20, '20%'], [21, '21%'], [22, '22%'], [23, '23%'], [24, '24%'], [25, '25%'], [26, '26%'], [27, '27%'], [28, '28%'], [29, '29%'], [30, '30%'], [31, '31%'], [32, '32%'], [33, '33%'], [34, '34%'], [35, '35%'], [36, '36%'], [37, '37%'], [38, '38%'], [39, '39%'], [40, '40%'], [41, '41%'], [42, '42%'], [43, '43%'], [44, '44%'], [45, '45%'], [46, '46%'], [47, '47%'], [48, '48%'], [49, '49%'], [50, '50%'], [51, '51%'], [52, '52%'], [53, '53%'], [54, '54%'], [55, '55%'], [56, '56%'], [57, '57%'], [58, '58%'], [59, '59%'], [60, '60%'], [61, '61%'], [62, '62%'], [63, '63%'], [64, '64%'], [65, '65%'], [66, '66%'], [67, '67%'], [68, '68%'], [69, '69%'], [70, '70%'], [71, '71%'], [72, '72%'], [73, '73%'], [74, '74%'], [75, '75%'], [76, '76%'], [77, '77%'], [78, '78%'], [79, '79%'], [80, '80%'], [81, '81%'], [82, '82%'], [83, '83%'], [84, '84%'], [85, '85%'], [86, '86%'], [87, '87%'], [88, '88%'], [89, '89%'], [90, '90%'], [91, '91%'], [92, '92%'], [93, '93%'], [94, '94%'], [95, '95%'], [96, '96%'], [97, '97%'], [98, '98%'], [99, '99%'], [100, '100%']], label='... 1,5 Grad zu begrenzen ', max=100, min=0)
    posterior_belief_20 = models.IntegerField(choices=[[0, '0%'], [1, '1%'], [2, '2%'], [3, '3%'], [4, '4%'], [5, '5%'], [6, '6%'], [7, '7%'], [8, '8%'], [9, '9%'], [10, '10%'], [11, '11%'], [12, '12%'], [13, '13%'], [14, '14%'], [15, '15%'], [16, '16%'], [17, '17%'], [18, '18%'], [19, '19%'], [20, '20%'], [21, '21%'], [22, '22%'], [23, '23%'], [24, '24%'], [25, '25%'], [26, '26%'], [27, '27%'], [28, '28%'], [29, '29%'], [30, '30%'], [31, '31%'], [32, '32%'], [33, '33%'], [34, '34%'], [35, '35%'], [36, '36%'], [37, '37%'], [38, '38%'], [39, '39%'], [40, '40%'], [41, '41%'], [42, '42%'], [43, '43%'], [44, '44%'], [45, '45%'], [46, '46%'], [47, '47%'], [48, '48%'], [49, '49%'], [50, '50%'], [51, '51%'], [52, '52%'], [53, '53%'], [54, '54%'], [55, '55%'], [56, '56%'], [57, '57%'], [58, '58%'], [59, '59%'], [60, '60%'], [61, '61%'], [62, '62%'], [63, '63%'], [64, '64%'], [65, '65%'], [66, '66%'], [67, '67%'], [68, '68%'], [69, '69%'], [70, '70%'], [71, '71%'], [72, '72%'], [73, '73%'], [74, '74%'], [75, '75%'], [76, '76%'], [77, '77%'], [78, '78%'], [79, '79%'], [80, '80%'], [81, '81%'], [82, '82%'], [83, '83%'], [84, '84%'], [85, '85%'], [86, '86%'], [87, '87%'], [88, '88%'], [89, '89%'], [90, '90%'], [91, '91%'], [92, '92%'], [93, '93%'], [94, '94%'], [95, '95%'], [96, '96%'], [97, '97%'], [98, '98%'], [99, '99%'], [100, '100%']], label='2 Grad zu begrenzen', max=100, min=0)
    time_pressure = models.BooleanField()
    give = models.CurrencyField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'], [11, '11'], [12, '12'], [13, '13'], [14, '14'], [15, '15'], [16, '16'], [17, '17'], [18, '18'], [19, '19'], [20, '20'], [21, '21']], label='Wie viel von den 21 Euro möchten Sie an atmosfair spenden?', max=21, min=0)
class Prior(Page):
    form_model = 'player'
    form_fields = ['prior_belief']
class News(Page):
    form_model = 'player'
    form_fields = ['pn1', 'pn2', 'pn3', 'pn4']
    @staticmethod
    def is_displayed(player: Player):
        return player.time_pressure == 0
class News_(Page):
    form_model = 'player'
    form_fields = ['nn1', 'nn2', 'nn3', 'nn4']
    @staticmethod
    def is_displayed(player: Player):
        return player.time_pressure == 1
class Posterior(Page):
    form_model = 'player'
    form_fields = ['posterior_belief_15', 'posterior_belief_20']
    @staticmethod
    def error_message(player: Player, values):
        pass
class D1(Page):
    form_model = 'player'
class D2(Page):
    form_model = 'player'
    form_fields = ['give']
page_sequence = [Prior, News, News_, Posterior, D1, D2]