import os
from tests.test_base import IosDebugTests
from iosdebug.start import start


class Test(IosDebugTests):
    def test_whole_start_process(self):
        start(IosDebugTests.START_TEST_PROJECT_PATH)

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AppDelegate.swift"
        )
        with open(target_file, "r") as file:
            content = file.read()
            assert (
                "let navigationController = ShakableNavigationController()" in content
            )

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "ContainerBuilder.swift"
        )
        with open(target_file, "r") as file:
            content = file.read()
            assert "registerMockAwesomeRepository(to: container)" in content

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AwesomeRepositoryImpl.swift"
        )
        with open(target_file, "r") as file:
            content = file.read()
            assert "// MARK: - Mock implementation" in content
