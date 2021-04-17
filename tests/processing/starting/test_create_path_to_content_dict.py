from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict


class Test(IosDebugTests):
    def test_create_path_to_content_dict(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        app_delegate_file_key = [
            key for key in path_to_content_dict.keys() if "AppDelegate" in key
        ][0]
        with open(app_delegate_file_key, "r") as file:
            content = file.read()
            assert content == path_to_content_dict[app_delegate_file_key]
