
import re

# Precompile regex patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in conf] for key, conf in Conf.items()}

with open("file.txt") as log_file:
    for log_line in log_file:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(log_line) for pattern in patterns):
                flag = False
                break
        if flag:
            print(log_line.strip())
