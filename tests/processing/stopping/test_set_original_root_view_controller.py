import os

from iosdebug.processing.create_path_to_content_dict import create_path_to_content_dict
from iosdebug.processing.stopping.set_original_root_view_controller import (
    set_original_root_view_controller,
)
from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files


class Test(IosDebugTests):
    def test_create_path_to_content_dict(self):
        target_file = (
            IosDebugTests.STOP_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp"
            + os.sep
            + "AppDelegate.swift"
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert "rootViewController = ShakableNavigationController()" in content

        files = find_swift_files(IosDebugTests.STOP_TEST_PROJECT_PATH)
        path_to_content_dict = create_path_to_content_dict(files)
        set_original_root_view_controller(
            files, path_to_content_dict, IosDebugTests.STOP_TEST_PROJECT_PATH
        )

        with open(target_file, "r") as file:
            content = file.read()
            assert (
                "localWindow.rootViewController = UINavigationController()" in content
            )
