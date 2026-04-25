
import re

# Load log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Precompile patterns to avoid recompiling in each loop
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in Conf[key]]
    for key in Conf.keys()
}

# Iterate through the log lines
for log_line in log_lines:
    flag = True
    for patterns in compiled_patterns.values():
        if any(pattern.match(log_line) for pattern in patterns):
            flag = False
            break
    if flag:
        print(log_line.strip())
