from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    first_name = (By.ID, 'firstName')
    last_name = (By.ID, 'lastName')
    email = (By.ID, 'email')
    comments = (By.ID, 'comments')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    confirmation_message = (By.ID, 'formSubmitMessage')

    def load(self, base_url: str):
        self.open(f'{base_url}/form.html')

    def submit_form(self, first_name: str, last_name: str, email: str, comments: str):
        self.type_text(self.first_name, first_name)
        self.type_text(self.last_name, last_name)
        self.type_text(self.email, email)
        self.type_text(self.comments, comments)
        self.click(self.submit_button)

    def get_confirmation_message(self) -> str:
        return self.get_text(self.confirmation_message)
