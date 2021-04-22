from iosdebug.constants import RUN_SCRIPT_PHASE_ID
from iosdebug.processing.stopping.remove_run_script_build_phase import (
    remove_run_script_build_phase,
)
import os
from tests.test_base import IosDebugTests


class Test(IosDebugTests):
    def test_remove_run_script_build_phase(self):
        remove_run_script_build_phase(IosDebugTests.STOP_TEST_PROJECT_PATH)
        target_file = (
            IosDebugTests.STOP_TEST_PROJECT_PATH
            + os.sep
            + "DebugModeTestApp.xcodeproj"
            + os.sep
            + "project.pbxproj"
        )

        with open(target_file, "r") as file:
            content = file.read()

            assert RUN_SCRIPT_PHASE_ID not in content
            assert (
                'shellScript = "/usr/bin/python3 ${PROJECT_DIR}/Scripts/.ios-debug_sync.py";'
                not in content
            )
            assert "BBF071DD2631DA3900DF13DA /* Sync debug mode */," not in content
