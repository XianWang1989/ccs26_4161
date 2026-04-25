
import re

# Assuming Conf is defined elsewhere
Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        patterns = [DateString + pattern for pattern in ConfLine]
        if any(re.match(pattern, LogLine) for pattern in patterns):
            flag = False
            break
    if flag:
        output_lines.append(LogLine.strip())

# Print all collected lines at once
print('\n'.join(output_lines))
