from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.drag_drop_page import DragDropPage
from pages.form_page import FormPage
from tests.base_test import BaseTest


class TestMouseKeyboardDragDrop(BaseTest):
    def test_keyboard_actions(self, base_url, logger):
        page = FormPage(self.driver, logger)
        page.load(base_url)
        actions = ActionChains(self.driver)
        first_name_input = page.find(page.first_name)
        actions.click(first_name_input).send_keys('Automation').send_keys(Keys.TAB).send_keys('Tester').perform()
        assert first_name_input.get_attribute('value') == 'Automation'

    def test_drag_and_drop(self, base_url, logger):
        page = DragDropPage(self.driver, logger)
        page.load(base_url)
        page.perform_drag_drop()
        assert page.get_drag_status() == 'Dropped successfully'
