from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FramePage(BasePage):
    sample_frame = (By.ID, 'sampleFrame')
    frame_text = (By.ID, 'frameText')

    def load(self, base_url: str):
        self.open(f'{base_url}/alerts_frames_windows.html')

    def get_frame_text(self) -> str:
        self.switch_to_frame(self.sample_frame)
        text = self.get_text(self.frame_text)
        self.switch_to_default_content()
        return text
