
import re

# Assuming Conf is defined and DateString is set
Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                flag = False
                break
        if not flag:
            break

    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once
print("\n".join(output_lines))
