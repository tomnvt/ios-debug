from iosdebug.processing.starting.get_mock_settings_and_mock_cursor import (
    get_mock_settings_and_mock_cursor,
)
import os
from tests.test_base import IosDebugTests
from iosdebug.processing.starting.write_mock_implementations import (
    write_mock_implementations,
)
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.starting.find_repository_protocols import (
    find_repository_protocols,
)
from iosdebug.processing.starting.get_protocols_to_protocol_functions_dict import (
    get_protocols_to_protocol_functions_dict,
)
from iosdebug.processing.starting.create_and_set_mock_manager import (
    create_and_set_mock_manager,
)


class Test(IosDebugTests):
    def test_create_and_set_mock_manager(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        protocols_to_functions_map = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )
        processed_mock_manager = get_mock_settings_and_mock_cursor(
            protocols_to_functions_map
        )

        write_mock_implementations(
            repository_protocols, path_to_content_dict, protocols_to_functions_map
        )
        create_and_set_mock_manager(files, path_to_content_dict, processed_mock_manager)

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AppDelegate.swift"
        )
        with open(target_file, "r") as file:
            content = file.read()
            assert "rootViewController = ShakableNavigationController()" in content
