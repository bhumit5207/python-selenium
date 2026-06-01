import pytest
from pages.form_page import FormPage
from tests.base_test import BaseTest
from utils.data_reader import DataReader


class TestForm(BaseTest):
    def test_form_submission_with_json_data(self, base_url, logger):
        """Submit the contact form using JSON data and verify the confirmation message."""
        data = DataReader.read_json('data/test_data.json')['form']
        page = FormPage(self.driver, logger)
        page.load(base_url)
        page.submit_form(data['first_name'], data['last_name'], data['email'], data['comments'])
        assert 'Form submitted' in page.get_confirmation_message()

    def test_email_input_type(self, base_url, logger):
        """Verify the email field is configured as an HTML email input."""
        data = DataReader.read_json('data/test_data.json')['form']
        page = FormPage(self.driver, logger)
        page.load(base_url)
        assert page.find(page.email).get_attribute('type') == 'email'
        page.submit_form(data['first_name'], data['last_name'], data['email'], data['comments'])
        assert 'Form submitted' in page.get_confirmation_message()

    def test_form_submission_with_empty_first_name(self, base_url, logger):
        """Verify edge case submission when the first name is left blank."""
        data = DataReader.read_json('data/test_data.json')['form']
        page = FormPage(self.driver, logger)
        page.load(base_url)
        page.submit_form('', data['last_name'], data['email'], data['comments'])
        assert page.get_confirmation_message() == 'Form submitted:'

    @pytest.mark.parametrize('row', DataReader.read_csv('data/test_data.csv'))
    def test_form_submission_with_csv_data(self, base_url, logger, row):
        """Submit the form using data-driven CSV rows and validate the submission result."""
        page = FormPage(self.driver, logger)
        page.load(base_url)
        page.submit_form(row['first_name'], row['last_name'], row['email'], row['comments'])
        assert 'Form submitted' in page.get_confirmation_message()
