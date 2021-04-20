""" sync command implementation """


from iosdebug.stop import stop
from iosdebug.start import start
import os
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.stopping import set_original_root_view_controller, store_mocked_implementations


def sync(path=os.getcwd()):
    """
    Syncs variants found in mocked repository function
    with values in MockManager settings dicttionary
    """
    stop(path)
    start(path)
