import os
from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files
from iosdebug.processing.stopping.remove_mock_registrations import (
    remove_mock_registrations,
)


class Test(IosDebugTests):
    def test_create_path_to_content_dict(self):
        target_file = (
            IosDebugTests.STOP_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "ContainerBuilder.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert "registerMockAwesomeRepository(to: container)" in content

        files = find_swift_files(IosDebugTests.STOP_TEST_PROJECT_PATH)
        remove_mock_registrations(files)

        with open(target_file, "r") as file:
            content = file.read()
            assert "registerMockAwesomeRepository(to: container)" not in content
