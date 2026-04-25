
import re
from concurrent.futures import ThreadPoolExecutor

# Load configuration
Conf = {
    # Example configuration
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3', 'pattern4']
}

DateString = '2024-07-03 '  # Adjust based on your needs

# Function to process each log line
def process_log_line(log_line):
    flag = True
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    return log_line.strip() if flag else None

# Read log file and process lines concurrently
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Use ThreadPoolExecutor to process log lines in parallel
with ThreadPoolExecutor() as executor:
    results = executor.map(process_log_line, log_lines)

# Print only non-None results
for result in results:
    if result:  # Check if result is not None
        print(result)
