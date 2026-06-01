from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilePage(BasePage):
    upload_input = (By.ID, 'fileUpload')
    upload_message = (By.ID, 'uploadMessage')
    download_link = (By.ID, 'downloadLink')

    def load(self, base_url: str):
        self.open(f'{base_url}/file-upload-download.html')

    def upload_file(self, file_path: str):
        self.find(self.upload_input).send_keys(file_path)

    def get_upload_message(self) -> str:
        return self.get_text(self.upload_message)

    def click_download(self):
        self.click(self.download_link)
