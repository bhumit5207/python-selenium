# Python Selenium Automation Framework

A complete production-ready Selenium automation framework in Python using Page Object Model (POM), Pytest, and reusable utilities.

## Framework Structure

- `config.json` - default framework configuration
- `.env.example` - environment overrides and CI settings
- `pytest.ini` - Pytest configuration, HTML reporting, Allure reporting, reruns, and markers
- `conftest.py` - fixtures, browser setup, logging, and screenshot-on-failure hooks
- `run_allure_report.py` - run tests and open Allure report automatically when complete
- `utils/` - config parser, browser factory, wait helpers, logging, data readers, API client
- `pages/` - page object model classes for reusable page behavior
- `tests/` - sample test cases covering login, form handling, dropdowns, alerts, frames, file upload, drag and drop, table validation, API validation
- `resources/` - sample HTML pages used for stable local UI tests
- `.github/workflows/python-selenium-ci.yml` - GitHub Actions CI pipeline

## Setup Instructions

1. Clone the repository into your local workspace.
2. Create a Python virtual environment and activate it:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and update values if needed:
   ```powershell
   Copy-Item .env.example .env
   ```
5. Run tests from the repository root.

## Execution Commands

- Run a single test file:
  ```powershell
  pytest tests/test_login.py
  ```
- Run multiple tests:
  ```powershell
  pytest tests/test_form.py tests/test_dropdown_checkbox_radio.py
  ```
- Run tagged tests:
  ```powershell
  pytest -m regression
  ```
- Run tests in parallel using xdist:
  ```powershell
  pytest -n auto
  ```
- Run headless execution:
  ```powershell
  pytest --headless
  ```
- Run tests with Allure reporting and open the report automatically:
  ```powershell
  python run_allure_report.py
  ```
- Run tests in debug mode with verbose logging:
  ```powershell
  pytest -s -vv
  ```

> Test descriptions are printed to the console automatically. Add a docstring to each test method and pytest will display it before execution.

## Allure Reporting

1. Install the Allure command-line tool for Windows, for example via Scoop or Chocolatey:
   ```powershell
   scoop install allure
   # or
   choco install allure
   ```
2. Run tests and generate Allure results:
   ```powershell
   pytest --alluredir=allure-results
   ```
3. Generate a static Allure report:
   ```powershell
   allure generate allure-results -o allure-report --clean
   ```
4. Open the generated report locally:
   ```powershell
   allure open allure-report
   ```

`run_allure_report.py` runs tests, generates the report, and opens it automatically when execution completes.

## CI/CD

GitHub Actions workflow is configured in `.github/workflows/python-selenium-ci.yml` to install dependencies, run tests, and publish HTML reports.

## Major Selenium Methods Used

- `driver.get(url)` - navigate to a page
- `driver.find_element(...)` / `find_elements(...)` - locate page elements
- `WebDriverWait(...).until(...)` - explicit wait for conditions
- `expected_conditions.visibility_of_element_located` - wait until element is visible
- `element.click()` - click a UI element
- `element.send_keys()` - enter text
- `ActionChains` - advanced mouse and keyboard interactions
- `switch_to.frame()` / `switch_to.default_content()` - frame handling
- `switch_to.alert` - alert dialog handling
- `window_handles` / `switch_to.window()` - window/tab switching
- `execute_script()` - execute JavaScript for scrolling and DOM work

## Notes

- Local HTML sample pages in `resources/` keep the example tests stable and offline-ready.
- `pytest-html` automatically generates `reports/report.html` on every run.
- Screenshots are captured on failure and embedded in the HTML report.
- `pytest-rerunfailures` retries failed tests once before final failure.
- `pytest-xdist` supports parallel execution with `-n auto`.
- Requests-based API validation is included in `tests/test_api_validation.py`.
- Data-driven tests can consume JSON and CSV data from `data/test_data.json` and `data/test_data.csv`.
