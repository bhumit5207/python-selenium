from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertPage(BasePage):
    js_alert_button = (By.ID, 'jsAlert')
    js_confirm_button = (By.ID, 'jsConfirm')
    js_prompt_button = (By.ID, 'jsPrompt')
    alert_result = (By.ID, 'alertResult')

    def load(self, base_url: str):
        self.open(f'{base_url}/alerts_frames_windows.html')

    def trigger_alert(self):
        self.click(self.js_alert_button)

    def trigger_confirm(self):
        self.click(self.js_confirm_button)
        return self.accept_alert()

    def trigger_confirm_and_dismiss(self):
        self.click(self.js_confirm_button)
        return self.dismiss_alert()

    def trigger_prompt(self, text: str):
        self.click(self.js_prompt_button)
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def trigger_prompt_and_dismiss(self):
        self.click(self.js_prompt_button)
        return self.dismiss_alert()

    def get_alert_result(self) -> str:
        return self.get_text(self.alert_result)
