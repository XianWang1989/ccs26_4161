
import re

# Read the log file
with open("file.txt") as log:
    # Precompute the patterns
    patterns = [DateString + pat for conf in Conf.values() for pat in conf]

    for log_line in log:
        # Check if any pattern matches the log line
        if not any(re.match(pat, log_line) for pat in patterns):
            print(log_line.strip())
