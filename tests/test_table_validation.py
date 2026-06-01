from selenium.webdriver.common.by import By
from pages.table_page import TablePage
from tests.base_test import BaseTest


class TestTableValidation(BaseTest):
    def test_table_contents(self, base_url, logger):
        page = TablePage(self.driver, logger)
        page.load(base_url)
        table_data = page.get_table_data()
        assert ['Alice', '29', 'New York'] in table_data
        assert page.find(page.table).tag_name == 'table'

    def test_table_row_count(self, base_url, logger):
        page = TablePage(self.driver, logger)
        page.load(base_url)
        rows = page.get_table_rows()
        assert len(rows) == 4
        assert len(rows[0].find_elements(By.TAG_NAME, 'th')) == 3

    def test_specific_cell_value(self, base_url, logger):
        page = TablePage(self.driver, logger)
        page.load(base_url)
        table_cells = page.find(page.table).find_elements(By.TAG_NAME, 'tr')[2].find_elements(By.TAG_NAME, 'td')
        assert table_cells[2].text == 'London'
