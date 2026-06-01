from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class WaitUtils:
    @staticmethod
    def wait_for_element(driver: WebDriver, locator: tuple, timeout: int = 15):
        try:
            return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as exc:
            raise TimeoutException(f'Element not visible after {timeout} seconds: {locator}') from exc

    @staticmethod
    def wait_for_clickable(driver: WebDriver, locator: tuple, timeout: int = 15):
        try:
            return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException as exc:
            raise TimeoutException(f'Element not clickable after {timeout} seconds: {locator}') from exc

    @staticmethod
    def wait_for_title_contains(driver: WebDriver, text: str, timeout: int = 15):
        try:
            return WebDriverWait(driver, timeout).until(EC.title_contains(text))
        except TimeoutException as exc:
            raise TimeoutException(f'Title does not contain {text} after {timeout} seconds') from exc

    @staticmethod
    def wait_for_alert(driver: WebDriver, timeout: int = 15):
        try:
            return WebDriverWait(driver, timeout).until(EC.alert_is_present())
        except TimeoutException as exc:
            raise TimeoutException('Alert did not appear within timeout') from exc

    @staticmethod
    def fluent_wait_for_element(driver: WebDriver, locator: tuple, timeout: int = 15, poll_frequency: float = 0.5):
        try:
            wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as exc:
            raise TimeoutException(f'Fluent wait timed out after {timeout} seconds for {locator}') from exc
