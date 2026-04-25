
import re
import sys

# Assuming Conf is a dictionary where each key has a list of patterns
Conf = {
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3']
}

# Precompile the regex patterns
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in Conf[key]]
    for key in Conf
}

# Open the log file
with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(LogLine) for pattern in patterns):
                flag = False
                break
        if flag:
            # Use sys.stdout.write for faster output
            sys.stdout.write(LogLine.strip() + '\n')
