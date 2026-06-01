from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxRadioPage(BasePage):
    checkbox_one = (By.ID, 'checkboxOne')
    checkbox_two = (By.ID, 'checkboxTwo')
    checkbox_result = (By.ID, 'checkboxResult')
    radio_one = (By.ID, 'radioOption1')
    radio_two = (By.ID, 'radioOption2')
    radio_result = (By.ID, 'radioResult')

    def load(self, base_url: str):
        self.open(f'{base_url}/dropdown-checkbox-radio.html')

    def toggle_checkboxes(self):
        self.click(self.checkbox_one)
        self.click(self.checkbox_two)

    def select_radio_option(self, option_id: str):
        locator = (By.ID, option_id)
        self.click(locator)

    def get_checkbox_result(self) -> str:
        return self.get_text(self.checkbox_result)

    def get_radio_result(self) -> str:
        return self.get_text(self.radio_result)
