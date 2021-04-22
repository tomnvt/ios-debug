import os
from distutils.dir_util import copy_tree


class IosDebugTests:

    TESTS_DIRECTORY = os.getcwd() + os.sep + "tests" + os.sep + 'TestProjects' + os.sep

    START_TEST_PROJECT_PATH = TESTS_DIRECTORY + "DebugModeTestApp_start"
    STOP_TEST_PROJECT_PATH = TESTS_DIRECTORY + "DebugModeTestApp_stop"
    SYNC_TEST_PROJECT_PATH = TESTS_DIRECTORY + "DebugModeTestApp_sync"

    ALL_TEST_PROJECTS = [
        START_TEST_PROJECT_PATH,
        STOP_TEST_PROJECT_PATH,
        SYNC_TEST_PROJECT_PATH,
    ]

    ORIGINAL_PROJECT_SUFFIC = "_orig"

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        for project in cls.ALL_TEST_PROJECTS:
            copy_tree(
                project + cls.ORIGINAL_PROJECT_SUFFIC,
                project,
            )

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass
