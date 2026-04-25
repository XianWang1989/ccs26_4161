
import re

# Open the log file
with open("file.txt") as log:
    # Precompile the patterns for efficiency
    patterns = [re.compile(DateString + pattern) for pattern in Conf.values()]

    for log_line in log:
        # Use a flag to check if any pattern matches
        if all(not pattern.match(log_line) for pattern in patterns):
            print(log_line.strip())
