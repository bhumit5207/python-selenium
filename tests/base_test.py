import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def base_setup(self, driver):
        self.driver = driver
