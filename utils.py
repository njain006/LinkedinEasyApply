import random
import time
import re

def generate_random_wait_time(min_time=1.5, max_time=2.9):
    return random.uniform(min_time, max_time)

def extract_text(text, pattern):
    match = re.search(pattern, text)
    return match.group(1) if match else None
