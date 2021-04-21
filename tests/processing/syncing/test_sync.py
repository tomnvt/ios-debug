import os
from tests.test_base import IosDebugTests
from iosdebug.sync import sync


class Test(IosDebugTests):
    def test_sync(self):
        sync(IosDebugTests.SYNC_TEST_PROJECT_PATH)
        return
        target_file = (
            IosDebugTests.SYNC_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AppDelegate.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert '"justAnotherFunction()": 0' in content
            assert (
                '"justAnotherFunction()": ["Original", "Mocked1", "Mocked2", "Mocked3"]'
                in content
            )

        target_file = (
            IosDebugTests.SYNC_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AwesomeRepositoryImpl.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert "func justAnotherFunction() -> Bool {" in content
