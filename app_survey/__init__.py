from otree.api import *


doc = """
First part of the experiment: Questionnaire on sociodemographics, elicit preference to charity and to others, 
trial round of slider task
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_choice(label):
    return models.IntegerField(
        label=label,
        choices=[
            [1, 'never'],
            [2, 'rarely'],
            [3, 'sometimes'],
            [4, 'often'],
            [5, 'regularly'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )


class Player(BasePlayer):
    age = models.IntegerField(
        min=18, max=100,
        label='Please indicate your age.'
    )

    gender = models.StringField(
        label='What is the gender you associate with?',
        widget=widgets.RadioSelectHorizontal,
        choices=['Male', 'Female', 'Diverse']
    )

    edu = models.StringField(
        label='Which is the highest level of education you have completed?',
        choices=[
            'No formal qualification',
            'Middle school/ Junior high school',
            'High School/ Senior high school',
            'Undergraduate degree (BA/BSc/other)',
            'Graduate degree (MA/MSc/MPhil/ other)',
            'Doctorate degree (PhD/other)',
            "Don't know or not applicable"

        ]
    )
    nationality = models.StringField(
        label='What is your nationality?',
        choices=[
            'United States',
            'United Kingdom',
            'Ireland',
            'Germany',
            'France',
            'Spain',
            'Afghanistan',
            'Aland Islands',
            'Albania',
            'Algeria',
            'American Samoa',
            'Andorra',
            'Angola',
            'Anguilla',
            'Antarctica',
            'Antigua and Barbuda',
            'Argentina',
            'Armenia',
            'Aruba',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bahrain',
            'Bangladesh',
            'Barbados',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bermuda',
            'Bhutan',
            'Bolivia',
            'Bonaire',
            'Bosnia and Herzegovina',
            'Botswana',
            'Bouvet Island',
            'Brazil',
            'British Indian Ocean Territory',
            'Brunei Darussalam',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cambodia',
            'Cameroon',
            'Canada',
            'Cape Verde',
            'Cayman Islands',
            'Central African Republic',
            'Chad',
            'Chile',
            'China',
            'Christmas Islands',
            'Cocos (Keeling) Islands',
            'Colombia',
            'Comoros',
            'Congo',
            'Congo the Democratic Republic of the',
            'Cook Islands',
            'Costa Rica',
            "Cote d'Ivoire",
            'Croatia',
            'Cuba',
            'Curacao',
            'Cyprus',
            'Czech Republic',
            'Denmark',
            'Djibouti',
            'Dominica',
            'Dominica Republic',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Eritrea',
            'Estonia',
            'Ethiopia',
            'Falkland Islands (Malvinas)',
            'Faroe Islands',
            'Fiji',
            'Finland',
            'French Guiana',
            'French Polynesia',
            'French Southern Territories',
            'Gabon',
            'Gambia',
            'Georgia',
            'Ghana',
            'Gibraltar',
            'Greece',
            'Greenland',
            'Grenada',
            'Guadeloupe',
            'Guam',
            'Guatemala',
            'Guernsey',
            'Guinea',
            'Guinea-Bissau',
            'Guyana',
            'Haiti',
            'Heard Island and McDonald Island',
            'Holy See (Vatican City State)',
            'Honduras',
            'Hong Kong',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Isle of Man',
            'Israel',
            'Italy',
            'Jamaica',
            'Japan',
            'Jersey',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Kiribati',
            'Korea',
            'Kuwait',
            'Kyrgyzstan',
            "Lao People's Democratic Republic",
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Lichtenstein',
            'Lithuania',
            'Luxembourg',
            'Macao',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Maldives',
            'Mali',
            'Malta',
            'Marshall Islands',
            'Martinique',
            'Mauritania',
            'Mauritius',
            'Mayotte',
            'Mexico',
            'Micronesia',
            'Moldova',
            'Monaco',
            'Mongolia',
            'Montenegro',
            'Montserrat',
            'Morocco',
            'Mozambique',
            'Myanmar',
            'Namibia',
            'Nauru',
            'Nepal',
            'Netherlands',
            'New Caledonia',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'Niue',
            'Norfolk Island',
            'Northern Mariana Islands',
            'Norway',
            'Oman',
            'Pakistan',
            'Palau',
            'Palestinian Territory',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Pitcairn',
            'Poland',
            'Portugal',
            'Puerto Rico',
            'Qatar',
            'Reunion',
            'Romania',
            'Russian Federation',
            'Rwanda',
            'Saint Barthelemy',
            'Saint Helena',
            'Saint Kitts and Nevis',
            'Saint Lucia',
            'Saint Martin (French part)',
            'Saint Pierre and Miquelon',
            'Saint Vincent and the Grenadines',
            'Samoa',
            'San Marino',
            'Sao Tome and Principe',
            'Saudi Arabia',
            'Senegal',
            'Serbia',
            'Seychelles',
            'Sierra Leone',
            'Singapore',
            'Sint Maarteen (Dutch part)',
            'Slovakia',
            'Slovenia',
            'Solomon Islands',
            'Somalia',
            'South Africa',
            'South Georgia and South Sandwich Islands',
            'South Sudan',
            'Sri Lanka',
            'Sudan',
            'Suriname',
            'Svalbard and Jan Mayen',
            'Swaziland',
            'Sweden',
            'Switzerland',
            'Syrian Arab Republic',
            'Taiwan',
            'Tajikistan',
            'Tanzania',
            'Thailand',
            'Timor-Leste',
            'Togo',
            'Tokelau',
            'Tonga',
            'Trinidad and Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'Turk and Caicos Islands',
            'Tuvalu',
            'Uganda',
            'Ukraine',
            'United Arab Emirates',
            'United States Minor Outlying Islands',
            'Uruguay',
            'Uzbekistan',
            'Vanuatu',
            'Venezuela, Bolivarian Republic of',
            'Vietnam',
            'Wallis and Futuna',
            'Western Shara',
            'Yemen',
            'Zambia',
            'Zimbabwe'
        ]
    )

    income = models.StringField(
        label='What is your income?',
        # scale from Polific personal income (GBP)* exchange rate 1 GBP:1.39 $
        choices=[
            'Less than $13,800',
            '$13,800 - $27,799',
            '$27,800 - $41,699',
            '$41,700 - $55,599',
            '$55,600 - $69,499',
            '$69,500 - $83,399',
            '$83,400 - $97,299',
            '$97,300 - $111,199',
            '$111,200 - $125,099',
            '$125,100 - $138,999',
            '$139,000 - $208,499',
            'More than $208,500',
            'Rather not say',
        ]
    )

    occupation = models.StringField(
        label='What is the type of your occupation?',
        widget=widgets.RadioSelectHorizontal,
        choices=['blue collar worker', 'white collar worker']
    )

    industry = models.StringField(
        label='In which industry are you working?',
        # Prolific industry classifications
        choices=[
            'Arts, Design, Entertainment and Recreation',
            'Aviation',
            'Broadcasting',
            'College, University and Adult Education',
            'Computer and Electronics Manufacturing',
            'Construction',
            'Education',
            'Emergency service',
            'Finance and Insurance',
            'Food processing and services',
            'Government and Public Administration',
            'Grocery',
            'Health Care and Social Assistance',
            'Homemaker',
            'Hotel and Food Services',
            'Information Services and Data Processing',
            'Legal Services',
            'Other Manufacturing',
            'Market Research',
            'Medical/ Healthcare',
            'Ministry',
            'Mining',
            'Nuclear Power, Oil and Gas',
            'Product Development',
            'Real Estate Rental and Leasing',
            'Religious',
            'Research laboratories',
            'Retail',
            'Sanitation',
            'Scientific or Technical Service',
            'Software',
            'Telecommunications',
            'Tourism and hospitality',
            'Transportation and Warehousing'
            'Utilities',
            'Veterinary',
            'Wholesale',
            'Video Games',
            'Other Industry'
        ]
    )

    DG_hypo = models.IntegerField(
        label='Please state how much of this hypothetical $10 endowment you would share with the other imaginary person.',
        min=0, max=10,
    )

    reciprocity_neg = models.IntegerField(
        label='How willing are you to punish someone who treats you unfairly, even if there may be costs for you?',
        min=0, max=10,
    )

    donated = make_choice('How often do you donate money to a charitable organization?')

    volunteering = make_choice('How often do you volunteer for a good cause?')


# PAGES
class Part1(Page):
    pass


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'edu', 'income', 'occupation', 'industry']


class DG(Page):
    form_model = 'player'
    form_fields = ['DG_hypo', 'reciprocity_neg']


class Donation(Page):
    form_model = 'player'
    form_fields = ['donated', 'volunteering']


page_sequence = [Part1, Demographics, DG, Donation]
