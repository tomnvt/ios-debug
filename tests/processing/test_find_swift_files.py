from tests.test_base import IosDebugTests
from iosdebug.processing.find_swift_files import find_swift_files

import os


class Test(IosDebugTests):
    def test_find_swift_files(self):
        files = find_swift_files(IosDebugTests.START_TEST_PROJECT_PATH)
        file_names = [file.split(os.sep)[-1] for file in files]
        assert "AwesomeRepository.swift" in file_names
        assert "AwesomeRepositoryImpl.swift" in file_names
        assert "ContainerBuilder.swift" in file_names
        assert "AppDelegate.swift" in file_names
