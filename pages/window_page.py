from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WindowPage(BasePage):
    new_window_button = (By.ID, 'newWindow')
    new_tab_button = (By.ID, 'newTab')
    result_text = (By.ID, 'windowResult')

    def load(self, base_url: str):
        self.open(f'{base_url}/alerts_frames_windows.html')

    def open_new_window(self):
        self.click(self.new_window_button)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def open_new_tab(self):
        self.click(self.new_tab_button)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def get_result_text(self) -> str:
        return self.get_text(self.result_text)
