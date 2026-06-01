import os
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.data_reader import DataReader


class TestLogin(BaseTest):
    def test_login_success(self, base_url, logger):
        """Verify that a valid user can log in successfully and the success message is displayed."""
        data = DataReader.read_json('data/test_data.json')['login']
        page = LoginPage(self.driver, logger)
        page.load(base_url)
        page.login(data['username'], data['password'])
        assert 'Login successful for admin' in page.get_login_message()

    def test_login_with_empty_username(self, base_url, logger):
        """Verify the login flow handles an empty username field as an edge case."""
        page = LoginPage(self.driver, logger)
        page.load(base_url)
        page.login('', 'password123')
        assert page.get_login_message().startswith('Login successful for')

    def test_login_with_special_characters(self, base_url, logger):
        """Verify login with special characters in the username field."""
        page = LoginPage(self.driver, logger)
        page.load(base_url)
        page.login('user!@#$', 'password123')
        assert 'Login successful for user!@#$' in page.get_login_message()
