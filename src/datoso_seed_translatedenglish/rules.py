"""Rules for the Translated English seed."""
from datoso_seed_translatedenglish.dats import TranslatedEnglishDat

rules = [
    {
        'name': 'TranslatedEnglish Dat',
        '_class': TranslatedEnglishDat,
        'seed': 't_en',
        'priority': 50,
        'rules': [
            {
                'key': 'name',
                'operator': 'contains',
                'value': '[T-En]',
            },
        ],
    },
]


def get_rules() -> list:
    """Get the rules."""
    return rules
