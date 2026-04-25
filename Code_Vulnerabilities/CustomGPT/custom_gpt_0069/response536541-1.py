
import re

# Assume Conf is defined earlier in your code
Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            combined_pattern = DateString + pattern
            if re.match(combined_pattern, LogLine):
                flag = False
                break 
        if not flag:
            break 
    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once
print("\n".join(output_lines))
