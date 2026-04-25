
import re
import sys

# Precompile regex patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

with open("file.txt") as log:
    for log_line in log:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(log_line) for pattern in patterns):
                flag = False
                break
        if flag:
            sys.stdout.write(log_line.strip() + "\n")
