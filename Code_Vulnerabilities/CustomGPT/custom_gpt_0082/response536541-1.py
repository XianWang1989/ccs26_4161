
import re

# Assume Conf is already defined with your patterns
Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            # Combine patterns directly with DateString
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                flag = False
                break
        if not flag:
            break

    if flag:
        output_lines.append(LogLine.strip())

# Print all lines at once to reduce the wait time
print("\n".join(output_lines))
