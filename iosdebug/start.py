import os
from .processing.find_swift_files import find_swift_files
from .processing.create_path_to_content_dict import create_path_to_content_dict
from .processing.starting import *


def start(path=os.getcwd()):
    swift_files = find_swift_files(path)

    path_to_content_map = create_path_to_content_dict(swift_files)

    repository_protocols = find_repository_protocols(path_to_content_map)

    protocol_to_protocol_functions = get_protocols_to_protocol_functions_dict(
        repository_protocols, path_to_content_map
    )

    registrations = get_registrations(repository_protocols)

    write_mock_implementations(
        repository_protocols, path_to_content_map, protocol_to_protocol_functions
    )

    processed_mock_manager = get_mock_settings_and_mock_cursor(
        protocol_to_protocol_functions
    )

    protocol_to_mocked_contents = get_protocol_to_mocked_content_dict(
        repository_protocols, path_to_content_map
    )

    store_mocked_implementation(protocol_to_mocked_contents)

    create_and_set_mock_manager(
        swift_files, path_to_content_map, processed_mock_manager
    )

    add_mock_registrations_to_container_builder(swift_files, registrations)
