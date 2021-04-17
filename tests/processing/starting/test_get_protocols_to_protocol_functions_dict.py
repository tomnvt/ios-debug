from tests.test_base import IosDebugTests
from iosdebug.processing.starting.get_protocols_to_protocol_functions_dict import (
    get_protocols_to_protocol_functions_dict,
)
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.starting.find_repository_protocols import (
    find_repository_protocols,
)


class Test(IosDebugTests):
    def test_get_protocols_to_protocol_functions_dict(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        repository_protocols = find_repository_protocols(path_to_content_dict)
        result = get_protocols_to_protocol_functions_dict(
            repository_protocols, path_to_content_dict
        )
        awesome_function = result["AwesomeRepository"][0]

        assert awesome_function.name == "doAwesomeThings"
        assert awesome_function.params == None
        assert awesome_function.return_type == None
