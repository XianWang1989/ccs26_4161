
import re

# Pre-compile the patterns for better performance
compiled_patterns = {}
for key, ConfLine in Conf.items():
    compiled_patterns[key] = [re.compile(DateString + pattern) for pattern in ConfLine]

with open("file.txt") as log_file:
    for log_line in log_file:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(log_line) for pattern in patterns):
                flag = False
                break
        if flag:
            print(log_line.strip())
