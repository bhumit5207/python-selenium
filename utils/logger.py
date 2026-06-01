import os
import logging
from logging.handlers import RotatingFileHandler


class LoggerManager:
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger('selenium_framework')
        self.logger.setLevel(getattr(logging, config.get('log_level', 'INFO').upper(), logging.INFO))
        self._configure_handlers()

    def _configure_handlers(self):
        if self.logger.handlers:
            return
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        log_dir = self.config.get('report_dir', 'reports')
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(os.path.join(log_dir, 'framework.log'), maxBytes=5_000_000, backupCount=3, encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
