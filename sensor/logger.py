import logging
import sys, os
from datetime import datetime


LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="w"
)

LOGGING = logging.getLogger()
