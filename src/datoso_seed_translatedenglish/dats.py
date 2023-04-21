"""
    TranslatedEnglish Dat class to parse different types of dat files.
"""
import re
from datoso.configuration import config
from datoso.repositories.dat import XMLDatFile

class TranslatedEnglishDat(XMLDatFile):
    """ Translated English Dat class. """
    seed: str = 't_en'

    def initial_parse(self):
        # pylint: disable=R0801
        """ Parse the dat file. """
        name = self.name

        name = name.split('[T-En]')[0].strip()
        name_array = name.split(' - ')

        company, system = name_array
        self.company = company
        self.system = system
        self.suffix = 'Translated-English'
        self.overrides()

        if self.modifier or self.system_type:
            self.preffix = config.get('PREFFIXES', self.modifier or self.system_type, fallback='')
        else:
            self.preffix = None

        return [self.preffix, self.company, self.system, self.suffix, self.get_date()]


    def get_date(self):
        """ Get the date from the dat file. """
        if self.file:
            result = re.findall(r'\(.*?\)', self.file)
            self.date = result[len(result)-1][1:-1]
        return self.date
