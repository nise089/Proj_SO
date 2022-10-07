from os import environ

SESSION_CONFIGS = [
    dict(
        name="sliders",
        display_name="RET Slider task",
        num_demo_participants=3,
        app_sequence=["app_sliders"],
    ),
    dict(
        name="profit",
        display_name="Profit choice",
        num_demo_participants=1,
        app_sequence=["app_decision_stage"],
    ),
    dict(
        name="founding",
        display_name="Founding choice",
        num_demo_participants=1,
        app_sequence=["app_founding_phase"],
    ),
    dict(
        name="production",
        display_name="Production",
        num_demo_participants=3,
        app_sequence=["app_production_phase"],
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1,
    participation_fee=0,
    wage=5,  # TODO set number from calibration
    piecerate=1,  # TODO set number from calibration
    productivity=2,  # TODO set number from calibration
    prod_piecerate=1,  # TODO find way to dynamically change == productivity - piecerate
    E=10,  # TODO set number from calibration
    Rfixed=10,  # TODO set number from calibration
    n=3,
    dividend=4,  # TODO set number from calibration
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['is_dropout']
SESSION_FIELDS = ['params']
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# adjustments for testing
# generating session configs for all varieties of features

import sys

if sys.argv[1] == 'test':
    MAX_ITERATIONS = 5
    FREEZE_TIME = 100
    TRIAL_PAUSE = 200
    TRIAL_TIMEOUT = 300

    SESSION_CONFIGS = [
        dict(
            name=f"testing_sliders",
            num_demo_participants=1,
            app_sequence=['sliders'],
            trial_delay=TRIAL_PAUSE / 1000.0,
            retry_delay=FREEZE_TIME / 1000.0,
            num_sliders=3,
            attempts_per_slider=3,
        )
    ]
