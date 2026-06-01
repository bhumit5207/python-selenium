from selenium.webdriver.common.by import By
from pages.alert_page import AlertPage
from pages.frame_page import FramePage
from pages.window_page import WindowPage
from tests.base_test import BaseTest


class TestAlertsFramesWindows(BaseTest):
    def test_alert_handling(self, base_url, logger):
        """Trigger browser alerts, confirmation dialogs, and prompts, and verify results."""
        page = AlertPage(self.driver, logger)
        page.load(base_url)
        page.trigger_alert()
        assert page.accept_alert() == 'This is an alert!'

        page.trigger_confirm()
        assert page.get_alert_result() == 'Confirmed'

        page.trigger_prompt('Selenium')
        assert page.get_alert_result() == 'Prompt accepted'

    def test_frame_handling(self, base_url, logger):
        """Switch into an iframe and verify the expected frame text is present."""
        page = FramePage(self.driver, logger)
        page.load(base_url)
        assert 'inside the frame' in page.get_frame_text().lower()

    def test_window_and_tab_handling(self, base_url, logger):
        """Open a new browser window or tab and verify the navigation result text."""
        page = WindowPage(self.driver, logger)
        page.load(base_url)
        page.open_new_window()
        assert 'New window or tab opened successfully' in page.get_result_text()

    def test_open_new_tab(self, base_url, logger):
        """Open a browser tab and verify the window count increases and result text is visible."""
        page = WindowPage(self.driver, logger)
        page.load(base_url)
        initial_handles = len(self.driver.window_handles)
        page.open_new_tab()
        assert len(self.driver.window_handles) == initial_handles + 1
        assert 'New window or tab opened successfully' in page.get_result_text()

    def test_confirm_cancel(self, base_url, logger):
        """Cancel the confirm dialog and verify the cancelled message is shown."""
        page = AlertPage(self.driver, logger)
        page.load(base_url)
        page.trigger_confirm_and_dismiss()
        assert page.get_alert_result() == 'Cancelled'

    def test_prompt_dismiss(self, base_url, logger):
        """Dismiss the prompt dialog and verify the prompt cancellation is shown."""
        page = AlertPage(self.driver, logger)
        page.load(base_url)
        page.trigger_prompt_and_dismiss()
        assert page.get_alert_result() == 'Prompt dismissed'

    def test_open_new_tab(self, base_url, logger):
        """Open a browser tab and verify the window count increases and result text is visible."""
        page = WindowPage(self.driver, logger)
        page.load(base_url)
        initial_handles = len(self.driver.window_handles)
        page.open_new_tab()
        assert len(self.driver.window_handles) == initial_handles + 1
        assert 'New window or tab opened successfully' in page.get_result_text()
