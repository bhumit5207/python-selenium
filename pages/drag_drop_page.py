from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DragDropPage(BasePage):
    source_item = (By.ID, 'dragSource')
    target_area = (By.ID, 'dropTarget')
    drag_status = (By.ID, 'dragStatus')

    def load(self, base_url: str):
        self.open(f'{base_url}/drag_drop.html')

    def perform_drag_drop(self):
        self.drag_and_drop(self.source_item, self.target_area)

    def get_drag_status(self) -> str:
        return self.get_text(self.drag_status)
