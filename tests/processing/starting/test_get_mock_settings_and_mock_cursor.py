from iosdebug.processing.starting.get_mock_settings_and_mock_cursor import (
    get_mock_settings_and_mock_cursor,
)
from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.starting.find_repository_protocols import (
    find_repository_protocols,
)
from iosdebug.processing.starting.get_protocols_to_protocol_functions_dict import (
    get_protocols_to_protocol_functions_dict,
)


class Test(IosDebugTests):
    def test_get_mock_settings_and_mock_cursor(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        protocols_to_functions_map = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )
        result = get_mock_settings_and_mock_cursor(protocols_to_functions_map)
        assert '"doAwesomeThings()": ["Mocked1", "Mocked2", "Mocked3"' in result
