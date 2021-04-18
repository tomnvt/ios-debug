from tests.test_base import IosDebugTests
from iosdebug.processing.starting.get_stored_mock_implementation import (
    get_stored_mock_implementation,
)


class Test(IosDebugTests):
    def test_get_stored_mock_implementation(self):
        result = get_stored_mock_implementation(
            IosDebugTests.START_TEST_PROJECT_PATH, "AwesomeRepository"
        )
        assert "class MockAwesomeRepositoryImpl" in result
