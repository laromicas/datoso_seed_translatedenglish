"""Actions for the Translated English seed."""
from datoso_seed_translatedenglish.dats import TranslatedEnglishDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': TranslatedEnglishDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions() -> dict:
    """Get the actions dictionary."""
    return actions
