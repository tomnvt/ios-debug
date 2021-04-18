from ast import literal_eval
import os
import pickle
from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.stopping.store_mocked_implementations import (
    store_mocked_implementations,
)
from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files


class Test(IosDebugTests):
    def test_create_path_to_content_dict(self):
        target_file = (
            IosDebugTests.STOP_TEST_PROJECT_PATH + os.sep + "ios-debug_data.pkl"
        )

        files = find_swift_files(IosDebugTests.STOP_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        store_mocked_implementations(
            path_to_content_dict, IosDebugTests.STOP_TEST_PROJECT_PATH
        )

        with open(target_file, "rb") as file:
            content = pickle.load(file)
            dictionary = literal_eval(content)
            print(dictionary)
            assert "mock_implementations" in dictionary
            assert "AwesomeRepository" in dictionary["mock_implementations"]
            assert (
                "func doAwesomeThings()"
                in dictionary["mock_implementations"]["AwesomeRepository"]
            )
