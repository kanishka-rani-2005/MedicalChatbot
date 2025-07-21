import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import os

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Define log file path
LOG_FILE = LOG_DIR / "app.log"

# Set up logger
logger = logging.getLogger("MedicalChatbotLogger")
logger.setLevel(logging.DEBUG)  # You can change to INFO or WARNING in production

# Formatter for logs
formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Rotating file handler (max 1MB, keep 5 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Optional: prevent logs from being duplicated if imported multiple times
logger.propagate = False
