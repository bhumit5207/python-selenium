from pages.checkbox_radio_page import CheckboxRadioPage
from pages.dropdown_page import DropdownPage
from tests.base_test import BaseTest


class TestDropdownCheckboxRadio(BaseTest):
    def test_dropdown_default_selection(self, base_url, logger):
        """Verify the dropdown initial value is displayed correctly on page load."""
        page = DropdownPage(self.driver, logger)
        page.load(base_url)
        assert page.get_selected_option() == 'Option 1'

    def test_dropdown_selection(self, base_url, logger):
        """Validate dropdown selection behavior and selected value display."""
        page = DropdownPage(self.driver, logger)
        page.load(base_url)
        page.select_option('Option 2')
        assert page.get_selected_option() == 'Option 2'

    def test_checkboxes_and_radio_buttons(self, base_url, logger):
        """Verify checkbox toggling and radio button selection update the page state."""
        page = CheckboxRadioPage(self.driver, logger)
        page.load(base_url)
        assert not page.find(page.checkbox_one).is_selected()
        assert not page.find(page.checkbox_two).is_selected()
        page.toggle_checkboxes()
        assert 'Checkbox 1' in page.get_checkbox_result()
        assert 'Checkbox 2' in page.get_checkbox_result()
        page.select_radio_option('radioOption2')
        assert page.get_radio_result() == 'Radio 2 selected'

    def test_radio_option_one_selection(self, base_url, logger):
        """Select the first radio option and verify the selection result."""
        page = CheckboxRadioPage(self.driver, logger)
        page.load(base_url)
        page.select_radio_option('radioOption1')
        assert page.get_radio_result() == 'Radio 1 selected'
