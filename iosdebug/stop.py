from .processing.find_swift_files import find_swift_files
from .processing.create_path_to_content_dict import create_path_to_content_dict
from .processing.stopping import *


def stop():
    swift_files = find_swift_files()
    path_to_content_map = create_path_to_content_dict(swift_files)
    store_mocked_implementations(path_to_content_map)
    set_original_root_view_controller(swift_files, path_to_content_map)
    remove_mock_registrations(swift_files)
