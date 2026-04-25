
import re
import sys

# Pre-compile patterns for efficiency
compiled_patterns = {}
for key, ConfLine in Conf.items():
    compiled_patterns[key] = [re.compile(DateString + pattern) for pattern in ConfLine]

with open("file.txt") as log:
    for log_line in log:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            sys.stdout.write(log_line.strip() + "\n")  # Buffered output
            sys.stdout.flush()  # Ensure immediate output
