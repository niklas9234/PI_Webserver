import logging
import sys
from logging.handlers import TimedRotatingFileHandler

class LoggingConfig:
    LOG_FILE = "../app.log"
    ROTATION_DAYS = 3

    @staticmethod
    def setup_logging():
        logger = logging.getLogger("webserver")
        logger.setLevel(logging.INFO)

        # Format
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = TimedRotatingFileHandler(LoggingConfig.LOG_FILE, when="D", interval=LoggingConfig.ROTATION_DAYS, backupCount=10, encoding="utf-8")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.INFO)

        # Console Logging
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_format)
        console_handler.setLevel(logging.INFO)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
