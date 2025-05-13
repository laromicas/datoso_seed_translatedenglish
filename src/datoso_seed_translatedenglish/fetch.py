"""Fetch and download DAT files."""
from datoso.configuration.folder_helper import Folders
from datoso_plugin_internetarchive.fetch import fetch_helper
from datoso_plugin_internetarchive.ia import Archive
from datoso_seed_translatedenglish import __prefix__


def fetch() -> None:
    """Fetch and download DAT files."""
    folder_helper = Folders(seed=__prefix__)
    folder_helper.clean_dats()
    folder_helper.create_all()
    archive = Archive(dat_folder='DATs', item='Retroplay-En-ROMs-2025')
    fetch_helper(archive, folder_helper, __prefix__)
