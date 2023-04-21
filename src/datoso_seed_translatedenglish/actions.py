from datoso_seed_translatedenglish.dats import TranslatedEnglishDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': TranslatedEnglishDat
        },
        {
            'action': 'DeleteOld'
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}'
        },
        {
            'action': 'SaveToDatabase'
        }
    ]
}

def get_actions():
    return actions