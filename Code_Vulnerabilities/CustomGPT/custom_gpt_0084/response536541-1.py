
import re

# Pre-compiled regex patterns
compiled_patterns = {}
for key, ConfLine in Conf.items():
    compiled_patterns[key] = [re.compile(DateString + pattern) for pattern in ConfLine]

with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(LogLine) for pattern in patterns):
                flag = False
                break 
        if flag:
            print(LogLine.strip())
