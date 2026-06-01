import json
import os
from pathlib import Path
from dotenv import load_dotenv


class ConfigParser:
    def __init__(self, root_path: Path):
        self.root_path = Path(root_path)
        self.config_file = self.root_path / 'config.json'
        self.env_file = self.root_path / '.env'

    def load_config(self) -> dict:
        if not self.config_file.exists():
            raise FileNotFoundError(f'Configuration file not found: {self.config_file}')
        with self.config_file.open('r', encoding='utf-8') as file:
            return json.load(file)

    def load_env(self, env_name: str = None) -> dict:
        env_path = self.env_file if env_name is None else self.root_path / f'.env.{env_name}'
        if not env_path.exists():
            raise FileNotFoundError(f'Environment file not found: {env_path}')
        load_dotenv(dotenv_path=env_path)
        return {
            'browser': os.getenv('BROWSER', 'chrome'),
            'headless': os.getenv('HEADLESS', 'True').lower() in ['true', '1', 'yes'],
            'base_url': os.getenv('BASE_URL', 'resources'),
            'timeout': int(os.getenv('TIMEOUT', 15)),
            'window_size': os.getenv('WINDOW_SIZE', '1920,1080'),
            'download_dir': os.getenv('DOWNLOAD_DIR', 'downloads'),
            'report_dir': os.getenv('REPORT_DIR', 'reports'),
            'log_level': os.getenv('LOG_LEVEL', 'INFO')
        }

    def resolve_base_url(self, base_url: str) -> str:
        if base_url.startswith('http://') or base_url.startswith('https://') or base_url.startswith('file://'):
            return base_url
        resolved_path = self.root_path / base_url
        return resolved_path.as_uri() if resolved_path.exists() else base_url
