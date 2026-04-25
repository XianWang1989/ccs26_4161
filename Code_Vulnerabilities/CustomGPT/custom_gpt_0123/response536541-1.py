
import re

# Open the log file
Log = open("file.txt")

# Pre-compile patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

for LogLine in Log:
    flag = True
    for key, regex_list in compiled_patterns.items():
        for pattern in regex_list:
            if pattern.match(LogLine):
                flag = False
                break
        if not flag:  # Exit early if a match is found
            break
    if flag:
        print(LogLine.strip())

Log.close()
