
import re

# Load configuration
Conf = {
    # Example structure: 'key': ['pattern1', 'pattern2']
    'example_key': ['pattern1', 'pattern2']
}

# Precompile regex patterns for better performance
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in ConfLine]
    for key, ConfLine in Conf.items()
}

# Open log file
with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(LogLine.strip())
