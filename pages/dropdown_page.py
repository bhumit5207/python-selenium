from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    select_menu = (By.ID, 'dropdown')
    selected_value_text = (By.ID, 'selectedValue')

    def load(self, base_url: str):
        self.open(f'{base_url}/dropdown-checkbox-radio.html')

    def select_option(self, visible_text: str):
        dropdown = self.find(self.select_menu)
        Select(dropdown).select_by_visible_text(visible_text)

    def get_selected_option(self) -> str:
        return self.get_text(self.selected_value_text)
