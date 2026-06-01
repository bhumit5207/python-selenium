from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    username_field = (By.ID, 'username')
    password_field = (By.ID, 'password')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    success_message = (By.ID, 'loginSuccess')

    def load(self, base_url: str):
        self.open(f'{base_url}/login.html')

    def login(self, username: str, password: str):
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click(self.submit_button)

    def get_login_message(self) -> str:
        return self.get_text(self.success_message)
