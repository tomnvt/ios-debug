import os
from tests.test_base import IosDebugTests
from iosdebug.stop import stop


class Test(IosDebugTests):
    def test_whole_start_process(self):
        stop(IosDebugTests.STOP_TEST_PROJECT_PATH)
