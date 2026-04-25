
import re

Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:
            break 
    if flag:
        output_lines.append(LogLine.strip())

# Print all lines at once
print("\n".join(output_lines))
