import os
import pathlib
from datetime import datetime


def capture_screenshot(driver, test_name: str) -> str:
    reports_dir = pathlib.Path(__file__).resolve().parents[1] / 'reports'
    reports_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_name = f'{test_name}_{timestamp}.png'
    screenshot_path = reports_dir / screenshot_name
    try:
        driver.save_screenshot(str(screenshot_path))
        return str(screenshot_path)
    except Exception:
        return ''
