
import re

# Open the log file
with open("file.txt") as log:
    # Precompile patterns for better performance
    compiled_patterns = []
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            compiled_patterns.append(re.compile(DateString + pattern))

    # Read through each log line
    for log_line in log:
        if all(not pattern.match(log_line) for pattern in compiled_patterns):
            print(log_line.strip())
