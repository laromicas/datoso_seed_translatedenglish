"""TranslatedEnglish Dat class to parse different types of dat files."""

import importlib.util
import logging
import re

from datoso.configuration import config
from datoso.repositories.dat_file import XMLDatFile


class TranslatedEnglishDat(XMLDatFile):
    """Translated English Dat class."""

    seed: str = 't_en'

    def initial_parse(self) -> list:
        # pylint: disable=R0801
        """Parse the dat file."""
        full_name = self.name

        name = full_name.split('[T-En]')[0].strip()
        if name == full_name:
            msg = f'Could not parse {full_name}. Expected format: <company> - <system> [T-En]'
            if importlib.util.find_spec('datoso_seed_enhanced'):
                logging.info(f'Using datoso_seed_enhanced for {full_name}')
                from datoso_seed_enhanced.dats import EnhancedDat
                enhanced = EnhancedDat(**self.__dict__)
                enhanced.initial_parse()
                self.file = enhanced.file
                self.seed = enhanced.seed
                self.data = enhanced.data
                self.main_key = enhanced.main_key
                self.header = enhanced.header
                self.name = enhanced.name
                self.full_name = enhanced.full_name
                self.date = enhanced.date
                self.homepage = enhanced.homepage
                self.url = enhanced.url
                self.author = enhanced.author
                self.email = enhanced.email
                self.game_key = enhanced.game_key
                self.suffix = enhanced.suffix
                self.company = enhanced.company
                self.system = enhanced.system
                self.system_type = enhanced.system_type
                self.prefix = enhanced.prefix
                return [self.prefix, self.company, self.system, self.suffix, self.get_date()]
            else:
                raise ValueError(msg)
        name_array = name.split(' - ')

        company, system = name_array
        self.company = company
        self.system = system
        self.suffix = 'Translated-English'
        self.overrides()

        if self.modifier or self.system_type:
            self.prefix = config.get('PREFIXES', self.modifier or self.system_type, fallback='')
        else:
            self.prefix = None

        return [self.prefix, self.company, self.system, self.suffix, self.get_date()]


    def get_date(self) -> str:
        """Get the date from the dat file."""
        if self.file:
            result = re.findall(r'\(.*?\)', str(self.file))
            self.date = result[len(result)-1][1:-1]
        return self.date
