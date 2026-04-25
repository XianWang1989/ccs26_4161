
import re
import sys

# Open the log file and configuration
Log = open("file.txt")
conf_patterns = {key: [DateString + pattern for pattern in conf_lines] for key, conf_lines in Conf.items()}

# Use a set for faster pattern matching
compiled_patterns = []
for conf_line in conf_patterns.values():
    compiled_patterns.extend(re.compile(pattern) for pattern in conf_line)

for LogLine in Log:
    flag = True
    for pattern in compiled_patterns:
        if pattern.match(LogLine):
            flag = False
            break
    if flag:
        # Print immediately using sys.stdout to reduce delay
        sys.stdout.write(LogLine.strip() + '\n')

Log.close()
