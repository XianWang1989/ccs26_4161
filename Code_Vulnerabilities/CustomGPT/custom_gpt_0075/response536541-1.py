
import re

# Read configuration
Conf = {
    'error': ['ERROR', 'FAILURE'],
    'warning': ['WARNING', 'CAUTION']
}

# Compile regex patterns for efficiency
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in conf_list] 
                     for key, conf_list in Conf.items()}

# Open the log file
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
            print(log_line.strip())
