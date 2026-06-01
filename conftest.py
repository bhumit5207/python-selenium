import os
import pathlib
import logging
import pytest
from utils.config_parser import ConfigParser
from utils.browser_factory import BrowserFactory
from utils.logger import LoggerManager
from utils.screenshot import capture_screenshot

ROOT_DIR = pathlib.Path(__file__).parent.resolve()
pytest_html = None


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None, help='Browser to use for tests: chrome, firefox, edge')
    parser.addoption('--headless', action='store_true', default=False, help='Run browser in headless mode')
    parser.addoption('--url', action='store', default=None, help='Base URL or local resource folder path')
    parser.addoption('--env', action='store', default=None, help='Environment name for config overrides')


@pytest.fixture(scope='session')
def config(request):
    browser_override = request.config.getoption('--browser')
    headless_override = request.config.getoption('--headless')
    url_override = request.config.getoption('--url')
    env_override = request.config.getoption('--env')

    parser = ConfigParser(ROOT_DIR)
    config = parser.load_config()

    if browser_override:
        config['browser'] = browser_override
    if headless_override:
        config['headless'] = True
    if url_override:
        config['base_url'] = url_override
    if env_override:
        config = parser.load_env(env_override)

    config['base_url'] = parser.resolve_base_url(config['base_url'])
    config['download_dir'] = os.path.join(ROOT_DIR, config['download_dir'])
    config['report_dir'] = os.path.join(ROOT_DIR, config['report_dir'])
    os.makedirs(config['download_dir'], exist_ok=True)
    os.makedirs(config['report_dir'], exist_ok=True)
    return config


@pytest.fixture(scope='session')
def logger(config):
    return LoggerManager(config).get_logger()


@pytest.fixture(scope='function')
def driver(request, config, logger):
    browser = config['browser']
    headless = config['headless']
    timeout = config['timeout']
    download_dir = config['download_dir']

    driver = BrowserFactory.get_driver(browser, headless, download_dir, config['window_size'])
    driver.maximize_window()
    driver.implicitly_wait(timeout)
    logger.info('Browser launched: %s | Headless: %s', browser, headless)

    def fin():
        if driver:
            driver.quit()
            logger.info('Browser closed')

    request.addfinalizer(fin)
    return driver


@pytest.fixture(scope='function')
def base_url(config):
    return config['base_url']


def _get_test_description(item):
    try:
        doc = item.function.__doc__
        if doc:
            return ' '.join(doc.split())
    except Exception:
        pass
    return item.name


def pytest_runtest_setup(item):
    description = _get_test_description(item)
    terminal_reporter = item.config.pluginmanager.getplugin('terminalreporter')
    message = f"\n=== RUNNING TEST: {item.nodeid} ===\nDescription: {description}\n"
    if terminal_reporter:
        terminal_reporter.write_line(message)
    else:
        print(message)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshot_path = capture_screenshot(driver, item.name)
            if screenshot_path and pytest_html is not None:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_path, mime_type='image/png'))
                report.extra = extra


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
    reports_path = ROOT_DIR / 'reports'
    if not reports_path.exists():
        os.makedirs(reports_path)
