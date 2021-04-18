from iosdebug.processing.starting.get_protocol_to_mocked_content_dict import (
    get_protocol_to_mocked_content_dict,
)
from iosdebug.processing.starting.get_mock_functions_variants import (
    get_mock_functions_variants,
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


class Test(IosDebugTests):
    def test_get_mock_functions_variants(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        protocols_to_functions_map = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )
        write_mock_implementations(
            repository_protocols,
            path_to_content_dict,
            protocols_to_functions_map,
            IosDebugTests.START_TEST_PROJECT_PATH,
        )

        protocol_to_mocked_contents = get_protocol_to_mocked_content_dict(
            repository_protocols, path_to_content_dict
        )

        result = get_mock_functions_variants(protocol_to_mocked_contents)[
            "AwesomeRepository"
        ]

        assert result["doAwesomeThings()"] == [
            '"Mocked1"',
            '"Mocked2"',
            '"Mocked3"',
            '"Mocked4"',
        ]

        assert result["doAwesomeThingsAndReturnSingle() -> Single<String>"] == [
            '"Mocked1"',
            '"Mocked2"',
            '"Mocked3"',
        ]
