import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from utils.wait_utils import WaitUtils


class BasePage:
    def __init__(self, driver: WebDriver, logger: logging.Logger):
        self.driver = driver
        self.logger = logger
        self.actions = ActionChains(driver)

    def open(self, url: str):
        self.logger.info('Opening URL: %s', url)
        self.driver.get(url)

    def find(self, locator: tuple):
        self.logger.debug('Finding element: %s', locator)
        return WaitUtils.wait_for_element(self.driver, locator)

    def click(self, locator: tuple):
        element = WaitUtils.wait_for_clickable(self.driver, locator)
        self.logger.info('Clicking on element: %s', locator)
        element.click()

    def type_text(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info('Typing text into element: %s', locator)

    def get_text(self, locator: tuple) -> str:
        element = self.find(locator)
        text = element.text
        self.logger.info('Getting text from element %s: %s', locator, text)
        return text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        element = self.find(locator)
        return element.get_attribute(attribute)

    def scroll_into_view(self, locator: tuple):
        element = self.find(locator)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def switch_to_frame(self, locator: tuple):
        frame = self.find(locator)
        self.driver.switch_to.frame(frame)
        self.logger.info('Switched to frame: %s', locator)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        self.logger.info('Switched to default content')

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        self.logger.info('Accepted alert with message: %s', text)
        return text

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.dismiss()
        self.logger.info('Dismissed alert with message: %s', text)
        return text

    def execute_script(self, script: str, *args):
        self.logger.info('Executing script: %s', script)
        return self.driver.execute_script(script, *args)

    def move_to_element(self, locator: tuple):
        element = self.find(locator)
        self.actions.move_to_element(element).perform()
        self.logger.info('Moved to element: %s', locator)

    def drag_and_drop(self, source_locator: tuple, target_locator: tuple):
        source = self.find(source_locator)
        target = self.find(target_locator)
        self.actions.drag_and_drop(source, target).perform()
        self.logger.info('Dragged %s to %s', source_locator, target_locator)

    def get_all_rows(self, locator: tuple):
        table = self.find(locator)
        return table.find_elements(By.TAG_NAME, 'tr')
