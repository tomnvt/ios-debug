from iosdebug.processing.starting.add_run_script_build_phase import (
    add_run_script_build_phase,
)
import os
from tests.test_base import IosDebugTests


class Test(IosDebugTests):
    def test_add_run_script_build_phase(self):
        add_run_script_build_phase(IosDebugTests.START_TEST_PROJECT_PATH)

        target_file = (
            IosDebugTests.START_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp.xcodeproj"
            + os.sep
            + "project.pbxproj"
        )

        with open(target_file, "r") as file:
            content = file.read()
            print("content")
            print(content)
            assert "BBF071DD2631DA3900DF13DA /* Sync debug mode */," in content
            assert (
                'shellScript = "/usr/bin/python3 ${PROJECT_DIR}/.ios-debug_sync.py";'
                in content
            )
