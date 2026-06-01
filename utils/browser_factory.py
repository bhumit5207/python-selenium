import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserFactory:
    @staticmethod
    def get_driver(browser: str, headless: bool, download_dir: str, window_size: str):
        browser = browser.lower()
        if browser == 'chrome':
            return BrowserFactory._create_chrome(headless, download_dir, window_size)
        if browser == 'firefox':
            return BrowserFactory._create_firefox(headless, download_dir, window_size)
        if browser == 'edge':
            return BrowserFactory._create_edge(headless, download_dir, window_size)
        raise ValueError(f'Unsupported browser: {browser}')

    @staticmethod
    def _create_chrome(headless: bool, download_dir: str, window_size: str):
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument(f'--window-size={window_size}')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        prefs = {
            'download.default_directory': os.path.abspath(download_dir),
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        }
        options.add_experimental_option('prefs', prefs)
        return webdriver.Chrome(options=options)

    @staticmethod
    def _create_firefox(headless: bool, download_dir: str, window_size: str):
        options = FirefoxOptions()
        if headless:
            options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.dir', os.path.abspath(download_dir))
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream, text/plain, application/pdf')
        driver = webdriver.Firefox(options=options, firefox_profile=profile)
        width, height = window_size.split(',')
        driver.set_window_size(int(width), int(height))
        return driver

    @staticmethod
    def _create_edge(headless: bool, download_dir: str, window_size: str):
        options = EdgeOptions()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument(f'--window-size={window_size}')
        prefs = {
            'download.default_directory': os.path.abspath(download_dir),
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        }
        options.add_experimental_option('prefs', prefs)
        return webdriver.Edge(options=options)
