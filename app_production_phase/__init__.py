import time
import json

from otree import settings
from otree.api import *

from _static.TimePage import TimePage
from .image_utils import encode_image
from . import task_sliders
import random



doc = """
Production Phase with
Slider task based on Github repository see code and documentation here: https://github.com/qwiglydee/otree-experiments
Profit choice and Selling choice
includes timeouts and dropout pages
"""


class Constants(BaseConstants):
    name_in_url = "production"
    players_per_group = 4
    num_rounds = 3  # TODO set number from calibration

    instructions_template = __name__ + "/instructions.html"


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    defaults = dict(
        trial_delay=1.0,
        retry_delay=0.1,
        num_sliders=48,  # adjust for more sliders to appear
        num_columns=3,
        attempts_per_slider=10
    )
    session.params = {}
    for param in defaults:
        session.params[param] = session.config.get(param, defaults[param])


class Group(BaseGroup):
    tot_effort = models.IntegerField()
    profit = models.IntegerField()
    price_offer = models.IntegerField(min=0, max=100)
    sold = models.BooleanField(initial=False)
    donation = models.IntegerField(initial=0)

    profit_choice = models.StringField(
        widget=widgets.RadioSelect,
        label='Please choose how the profit should be used.',
        choices=['owner bonus', 'worker bonus', 'donation']
    )

    accepted_price = models.IntegerField(
        min=0,
        max=100,  # TODO adjust accr. calibration
        label='Your price offer:'
    )

    has_dropout = models.BooleanField(initial=False)


class Player(BasePlayer):
    iteration = models.IntegerField(initial=0)

    num_correct = models.IntegerField(initial=0)
    elapsed_time = models.FloatField(initial=0)
    sold = models.StringField(initial='not sold')

    is_dropout = models.BooleanField(initial=False)


# puzzle-specific stuff
class Puzzle(ExtraModel):
    """A model to keep record of sliders setup"""

    player = models.Link(Player)
    iteration = models.IntegerField()
    timestamp = models.FloatField()

    num_sliders = models.IntegerField()
    layout = models.LongStringField()

    response_timestamp = models.FloatField()
    num_correct = models.IntegerField(initial=0)
    is_solved = models.BooleanField(initial=False)


class Slider(ExtraModel):
    """A model to keep record of each slider"""

    puzzle = models.Link(Puzzle)
    idx = models.IntegerField()
    target = models.IntegerField()
    value = models.IntegerField()
    is_correct = models.BooleanField(initial=False)
    attempts = models.IntegerField(initial=0)


def generate_puzzle(player: Player) -> Puzzle:
    """Create new puzzle for a player"""
    params = player.session.params
    num = params['num_sliders']
    layout = task_sliders.generate_layout(params)
    puzzle = Puzzle.create(
        player=player, iteration=player.iteration, timestamp=time.time(),
        num_sliders=num,
        layout=json.dumps(layout)
    )
    for i in range(num):
        target, initial = task_sliders.generate_slider()
        Slider.create(
            puzzle=puzzle,
            idx=i,
            target=target,
            value=initial
        )
    return puzzle


def get_current_puzzle(player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def get_slider(puzzle, idx):
    sliders = Slider.filter(puzzle=puzzle, idx=idx)
    if sliders:
        [puzzle] = sliders
        return puzzle


def encode_puzzle(puzzle: Puzzle):
    """Create data describing puzzle to send to client"""
    layout = json.loads(puzzle.layout)
    sliders = Slider.filter(puzzle=puzzle)
    # generate image for the puzzle
    image = task_sliders.render_image(layout, targets=[s.target for s in sliders])
    return dict(
        image=encode_image(image),
        size=layout['size'],
        grid=layout['grid'],
        sliders={s.idx: {'value': s.value, 'is_correct': s.is_correct} for s in sliders}
    )


def get_progress(player: Player):
    """Return current player progress"""
    return dict(
        iteration=player.iteration,
        solved=player.num_correct
    )


def handle_response(puzzle, slider, value):
    slider.value = task_sliders.snap_value(value, slider.target)
    slider.is_correct = slider.value == slider.target
    puzzle.num_correct = len(Slider.filter(puzzle=puzzle, is_correct=True))
    puzzle.is_solved = puzzle.num_correct == puzzle.num_sliders


def play_game(player: Player, message: dict):
    """Main game workflow
    Implemented as reactive scheme: receive message from browser, react, respond.

    Generic game workflow, from server point of view:
    - receive: {'type': 'load'} -- empty message means page loaded
    - check if it's game start or page refresh midgame
    - respond: {'type': 'status', 'progress': ...}
    - respond: {'type': 'status', 'progress': ..., 'puzzle': data}
      in case of midgame page reload

    - receive: {'type': 'new'} -- request for a new puzzle
    - generate new sliders
    - respond: {'type': 'puzzle', 'puzzle': data}

    - receive: {'type': 'value', 'slider': ..., 'value': ...} -- submitted value of a slider
      - slider: the index of the slider
      - value: the value of slider in pixels
    - check if the answer is correct
    - respond: {'type': 'feedback', 'slider': ..., 'value': ..., 'is_correct': ..., 'is_completed': ...}
      - slider: the index of slider submitted
      - value: the value aligned to slider steps
      - is_corect: if submitted value is correct
      - is_completed: if all sliders are correct
    """
    session = player.session
    my_id = player.id_in_group
    params = session.params

    now = time.time()
    # the current puzzle or none
    puzzle = get_current_puzzle(player)

    message_type = message['type']

    if message_type == 'load':
        p = get_progress(player)
        if puzzle:
            return {my_id: dict(type='status', progress=p, puzzle=encode_puzzle(puzzle))}
        else:
            return {my_id: dict(type='status', progress=p)}

    if message_type == "new":
        if puzzle is not None:
            raise RuntimeError("trying to create 2nd puzzle")

        player.iteration += 1
        z = generate_puzzle(player)
        p = get_progress(player)

        return {my_id: dict(type='puzzle', puzzle=encode_puzzle(z), progress=p)}

    if message_type == "value":
        if puzzle is None:
            raise RuntimeError("missing puzzle")
        if puzzle.response_timestamp and now < puzzle.response_timestamp + params["retry_delay"]:
            raise RuntimeError("retrying too fast")

        slider = get_slider(puzzle, int(message["slider"]))

        if slider is None:
            raise RuntimeError("missing slider")
        if slider.attempts >= params['attempts_per_slider']:
            raise RuntimeError("too many slider motions")

        value = int(message["value"])
        handle_response(puzzle, slider, value)
        puzzle.response_timestamp = now
        slider.attempts += 1
        player.num_correct = puzzle.num_correct

        p = get_progress(player)
        return {
            my_id: dict(
                type='feedback',
                slider=slider.idx,
                value=slider.value,
                is_correct=slider.is_correct,
                is_completed=puzzle.is_solved,
                progress=p,
            )
        }

    if message_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type='solution', solution={s.idx: s.target for s in Slider.filter(puzzle=puzzle)})}

    raise RuntimeError("unrecognized message from client")


# Pages
class WorkingStage(TimePage):
    timeout_seconds = 20

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.id_in_group != 1


class Game(Page):
    timeout_seconds = 120

    live_method = play_game

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.id_in_group != 1

    @staticmethod
    def js_vars(player: Player):
        return dict(
            params=player.session.params,
            slider_size=task_sliders.SLIDER_BBOX,
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            params=player.session.params,
            DEBUG=settings.DEBUG
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        puzzle = get_current_puzzle(player)

        if puzzle and puzzle.response_timestamp:
            player.elapsed_time = puzzle.response_timestamp - puzzle.timestamp
            player.num_correct = puzzle.num_correct


class WorkWaitPage(WaitPage):
    # use own template
    template_name = 'app_production_phase/WorkWaitPage.html'

    @staticmethod
    def set_profit(group: Group):
        players = group.get_players()
        effort = [p.num_correct for p in players]
        group.tot_effort = sum(effort)
        revenue = settings.SESSION_CONFIG_DEFAULTS['prod_piecerate'] * group.tot_effort
        group.profit = revenue + settings.SESSION_CONFIG_DEFAULTS['Rfixed'] \
                       - settings.SESSION_CONFIG_DEFAULTS['n'] * settings.SESSION_CONFIG_DEFAULTS['wage'] \
                       - settings.SESSION_CONFIG_DEFAULTS['dividend']

    after_all_players_arrive = set_profit


class ProfitChoice(TimePage):
    timeout_seconds = 120  # set timeout for page

    form_model = 'group'
    form_fields = ['profit_choice']

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.id_in_group == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        TimePage.before_next_page(player, timeout_happened)
        group = player.group
        if group.profit_choice == 'donation':
            group.donation = group.profit


class SellingChoice(TimePage):
    timeout_seconds = 120

    form_model = 'group'
    form_fields = ['accepted_price']

    @staticmethod
    def is_displayed(player: Player):
        parent_condition = TimePage.is_displayed(player)
        return parent_condition and player.id_in_group == 1


def company_sold(group: Group):
    # draw a random price offer from normal distribution 0 - 100
    group.price_offer = random.randint(0, 100)
    print('Z is ', group.price_offer)
    price = group.field_maybe_none('accepted_price')
    if price is None:  # check is selling decision was made
        return
    # check if offered price >= accepted price
    # if true, switch sold to true
    elif group.price_offer >= price:
        group.sold = True
        print('company is sold is ', group.sold)
    else:
        print('company is sold is ', group.sold)


class ChoiceWaitPage(WaitPage):
    # use own template
    template_name = 'app_production_phase/ChoiceWaitPage.html'

    # for later sum up all payoffs across rounds
    # if player.round_number == 1:
    #     player.payoff = settings.SESSION_CONFIG_DEFAULTS['wage'] + puzzle.num_correct * \
    #                     settings.SESSION_CONFIG_DEFAULTS['piecerate']
    # else:
    #     prev_player = player.in_round(player.round_number - 1)
    #     prev_payoff = prev_player.payoff
    #     player.payoff = prev_payoff + settings.SESSION_CONFIG_DEFAULTS['wage'] + puzzle.num_correct * \
    #                     settings.SESSION_CONFIG_DEFAULTS['piecerate']

    @staticmethod
    def set_payoffs(group: Group):
        # computer price offer and selling consequence
        company_sold(group)
        profit_choice = group.field_maybe_none('profit_choice')
        # payoffs
        if profit_choice is None:  # check if profit choice was made
            # if not, also no selling choice must have been made
            for p in group.get_players():
                # investor payoff
                if p.id_in_group == 1:
                    p.payoff = settings.SESSION_CONFIG_DEFAULTS['dividend']
                # worker payoff
                else:
                    p.payoff = settings.SESSION_CONFIG_DEFAULTS['wage'] \
                            + p.num_correct * settings.SESSION_CONFIG_DEFAULTS['piecerate']
        else:
            for p in group.get_players():
                # investor payoff
                if p.id_in_group == 1:
                    p.payoff = settings.SESSION_CONFIG_DEFAULTS['dividend']
                    if profit_choice == 'owner bonus':
                        p.payoff += group.profit
                        if group.sold:
                            p.payoff += group.price_offer
                    elif profit_choice != 'owner bonus' and group.sold:
                        p.payoff += group.price_offer
                # worker payoff
                else:
                    p.payoff = settings.SESSION_CONFIG_DEFAULTS['wage'] \
                            + p.num_correct * settings.SESSION_CONFIG_DEFAULTS['piecerate']
                    if profit_choice == 'worker bonus':
                        p.payoff += group.profit / 3

    after_all_players_arrive = set_payoffs


class ResultsChoice(TimePage):
    pass


class Dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.is_dropout


class DropoutVictim(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout and player.is_dropout is False


page_sequence = [WorkingStage, Game, WorkWaitPage, ProfitChoice, SellingChoice, ChoiceWaitPage,
                 ResultsChoice, Dropout, DropoutVictim]
