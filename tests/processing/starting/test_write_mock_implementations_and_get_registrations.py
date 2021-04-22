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
from iosdebug.constants import DATA_FILE, KEY_MOCK_IMPLEMENTATIONS
import pickle


class Test(IosDebugTests):
    def test_write_mock_implementations(self):
        path = IosDebugTests.START_TEST_PROJECT_PATH
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        with open(path + os.sep + DATA_FILE, "wb") as file:
            pickle.dump(str({KEY_MOCK_IMPLEMENTATIONS: ""}), file)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        protocols_to_functions_map = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )
        write_mock_implementations(
            path_to_content_dict,
            protocols_to_functions_map,
            IosDebugTests.START_TEST_PROJECT_PATH,
        )

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AwesomeRepository.swift"
        )
        with open(target_file, "r") as file:
            content = file.read()
            assert "// MARK: - Mock implementation" in content
            assert content.count("func doGenericAwesomeThings<T>") == 2
            assert (
                content.count("func doAwesomeThingsAndReturnSingle() -> Single<String>")
                == 2
            )

            assert (
                """\
    container.register(AwesomeRepositoryImpl.self) { _ in
        AwesomeRepositoryImpl()
    }
""".strip()
                in content
            )
