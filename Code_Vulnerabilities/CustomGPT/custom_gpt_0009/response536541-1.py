
import re

Log = open("file.txt")
output_lines = []  # List to store lines to be printed

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:  # This is more readable
            break 
    if flag:
        output_lines.append(LogLine.strip())  # Collect line instead of printing

# Print all at once
print('\n'.join(output_lines))
