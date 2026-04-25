
import re
from concurrent.futures import ThreadPoolExecutor

# Precompile your patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

def process_log_line(log_line):
    for key, patterns in compiled_patterns.items():
        if any(pattern.match(log_line) for pattern in patterns):
            return None  # Skip matching lines
    return log_line.strip()  # Return the line if it doesn't match

# Open the log file
with open("file.txt") as log:
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_log_line, log)

# Print results
for result in results:
    if result is not None:
        print(result)
