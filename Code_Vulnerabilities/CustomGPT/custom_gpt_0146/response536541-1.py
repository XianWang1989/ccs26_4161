
import re

# Read the log file
with open("file.txt") as log_file:
    # Precompiled regex patterns
    compiled_patterns = {
        key: [re.compile(DateString + pattern) for pattern in conf_line]
        for key, conf_line in Conf.items()
    }

    for log_line in log_file:
        if not any(any(pattern.match(log_line) for pattern in patterns) for patterns in compiled_patterns.values()):
            print(log_line.strip())
