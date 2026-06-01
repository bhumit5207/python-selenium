from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TablePage(BasePage):
    table = (By.ID, 'sampleTable')

    def load(self, base_url: str):
        self.open(f'{base_url}/table.html')

    def get_table_rows(self):
        return self.find(self.table).find_elements(By.TAG_NAME, 'tr')

    def get_table_data(self):
        rows = self.get_table_rows()[1:]
        data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            data.append([cell.text for cell in cells])
        return data

    def find_cell_text(self, row_index: int, column_index: int) -> str:
        row = self.get_table_rows()[row_index]
        cells = row.find_elements(By.TAG_NAME, 'td')
        return cells[column_index].text
