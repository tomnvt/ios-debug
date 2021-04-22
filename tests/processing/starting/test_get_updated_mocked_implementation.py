from iosdebug.processing.starting.get_mock_functions_variants import (
    get_mock_functions_variants,
)
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.starting.find_repository_protocols import (
    find_repository_protocols,
)
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.starting.get_protocols_to_protocol_functions_dict import (
    get_protocols_to_protocol_functions_dict,
)
from iosdebug.processing.starting.get_updated_mocked_implementation import (
    get_updated_mocked_implementation,
)
from iosdebug.processing.starting.get_stored_mock_implementation import (
    get_stored_mock_implementation,
)
from tests.test_base import IosDebugTests
from iosdebug.sync import sync


class Test(IosDebugTests):
    def test_get_updated_mocked_implementation(self):
        files = find_swift_files(IosDebugTests.SYNC_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        protocols_to_protocol_functions_dict = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )

        stored_impl = get_stored_mock_implementation(
            IosDebugTests.SYNC_TEST_PROJECT_PATH, "AwesomeRepository"
        )
        mock_functions_variants = get_mock_functions_variants(
            {"AwesomeRepository": stored_impl}
        )

        result = get_updated_mocked_implementation(
            protocols_to_protocol_functions_dict["AwesomeRepository"],
            stored_impl,
            list(mock_functions_variants["AwesomeRepository"].keys()),
        )

        assert "justAnotherFunction(param: Bool) -> Bool {" in result
        assert "justAnotherFunction() -> Bool {" not in result
        assert "doAwesomeThings() {" not in result
