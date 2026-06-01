import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
ALLURE_RESULTS = ROOT_DIR / 'allure-results'
ALLURE_REPORT = ROOT_DIR / 'allure-report'


def check_allure_installed() -> str:
    path = shutil.which('allure')
    return path or ''


def run_pytest() -> int:
    command = [sys.executable, '-m', 'pytest', '--alluredir', str(ALLURE_RESULTS)]
    return subprocess.run(command, cwd=ROOT_DIR).returncode


def generate_allure_report(allure_path: str) -> int:
    if ALLURE_REPORT.exists():
        shutil.rmtree(ALLURE_REPORT)
    command = [allure_path, 'generate', str(ALLURE_RESULTS), '-o', str(ALLURE_REPORT), '--clean']
    return subprocess.run(command, cwd=ROOT_DIR, shell=False).returncode


def open_allure_report(allure_path: str) -> int:
    command = [allure_path, 'open', str(ALLURE_REPORT)]
    return subprocess.run(command, cwd=ROOT_DIR, shell=False).returncode


if __name__ == '__main__':
    allure_path = check_allure_installed()
    if not allure_path:
        print('ERROR: Allure command-line tool is not installed. Install it using Scoop or Chocolatey and try again.')
        sys.exit(1)

    ALLURE_RESULTS.mkdir(exist_ok=True)

    print('Running pytest with Allure result collection...')
    exit_code = run_pytest()
    if exit_code != 0:
        print(f'pytest failed with exit code {exit_code}. Allure results may still be available in {ALLURE_RESULTS}')

    print('Generating Allure report...')
    report_code = generate_allure_report(allure_path)
    if report_code != 0:
        print('Failed to generate Allure report. Please verify allure installation and result files.')
        sys.exit(report_code)

    print('Opening Allure report in the browser...')
    open_code = open_allure_report(allure_path)
    if open_code != 0:
        print('Failed to open Allure report. You can open it manually with: allure open allure-report')
        sys.exit(open_code)

    sys.exit(exit_code)
