
import re

# Load log and patterns
log_file = open("file.txt")
patterns_set = {DateString + pattern for conf in Conf.values() for pattern in conf}

# Read from the log and check against patterns
for log_line in log_file:
    if not any(re.match(pattern, log_line) for pattern in patterns_set):
        print(log_line.strip(), flush=True)  # Ensure immediate output
