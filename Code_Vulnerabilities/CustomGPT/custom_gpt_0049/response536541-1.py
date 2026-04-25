
import re

Log = open("file.txt")
output_lines = []  # List to hold the lines to print

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

# Print all at once to reduce delays
print("\n".join(output_lines))
