
import re

# Assume Conf is a dictionary structured as {key: [list_of_patterns]}
# Example:
# Conf = {'key1': ['pattern1', 'pattern2'], 'key2': ['pattern3']}

# Pre-compile patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in patterns] for key, patterns in Conf.items()}

with open("file.txt") as log_file:
    for log_line in log_file:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(log_line.strip())
