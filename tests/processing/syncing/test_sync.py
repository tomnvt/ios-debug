import os
from tests.test_base import IosDebugTests
from iosdebug.start import start
from iosdebug.stop import stop


class Test(IosDebugTests):
    def test_sync(self):
        stop(IosDebugTests.SYNC_TEST_PROJECT_PATH, False)
        start(IosDebugTests.SYNC_TEST_PROJECT_PATH, False)

        target_file = (
            IosDebugTests.SYNC_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AppDelegate.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            print(content)
            assert '"justAnotherFunction(param:)": 0' in content
            assert (
                '"justAnotherFunction(param:)": ["Original", "Mocked1", "Mocked2", "Mocked3"]'
                in content
            )

        target_file = (
            IosDebugTests.SYNC_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AwesomeRepository.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert "func justAnotherFunction(param: Bool) -> Bool {" in content
