
import re
import sys

# Load log file
Log = open("file.txt")
output_lines = []

# Pre-compile regex patterns
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in ConfLine]
    for key, ConfLine in Conf.items()
}

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
        output_lines.append(LogLine.strip())

# Print all lines at once
sys.stdout.write('\n'.join(output_lines) + '\n')

# Close the log file
Log.close()
