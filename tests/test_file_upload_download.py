import os
from selenium.webdriver.common.by import By
from pages.file_page import FilePage
from tests.base_test import BaseTest


class TestFileUploadDownload(BaseTest):
    def test_file_upload_and_download_link(self, base_url, logger):
        """Upload a sample file and verify download link metadata is correct."""
        page = FilePage(self.driver, logger)
        page.load(base_url)
        upload_file = os.path.abspath('data/upload_test.txt')
        page.upload_file(upload_file)
        assert 'Uploaded: upload_test.txt' in page.get_upload_message()
        page.click_download()
        download_link = self.driver.find_element(By.ID, 'downloadLink')
        assert download_link.get_attribute('download') == 'sample.txt'

    def test_download_link_has_correct_href(self, base_url, logger):
        """Verify the download link URL and download attribute are correct."""
        page = FilePage(self.driver, logger)
        page.load(base_url)
        download_element = page.find(page.download_link)
        assert download_element.get_attribute('download') == 'sample.txt'
        assert 'Sample%20download%20content' in download_element.get_attribute('href')
