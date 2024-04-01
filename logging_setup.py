import logging
import os
from datetime import datetime

def setup_logger():
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%H:%M:%S')

    # Create logs directory if not exists
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # File handler
    log_file = os.path.join('logs', datetime.now().strftime("%m_%d_%y_%H_%M_%S") + '_applyJobs.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

    return log

log = setup_logger()
