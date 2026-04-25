
import re

# Assuming Conf is defined somewhere
Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        if any(re.match(DateString + pattern, LogLine) for pattern in ConfLine):
            flag = False
            break
    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once
print("\n".join(output_lines))
