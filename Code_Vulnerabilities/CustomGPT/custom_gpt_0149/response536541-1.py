
import re

Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            pattern = DateString + pattern
            if re.match(pattern, LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        output_lines.append(LogLine.strip())

# Print all at once
print("\n".join(output_lines))
