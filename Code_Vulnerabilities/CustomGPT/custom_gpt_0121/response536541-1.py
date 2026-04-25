
import re

Log = open("file.txt")
output = []  # Store lines to print later

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                flag = False
                break 
        if not flag:  # Exit if match is found
            break 
    if flag:
        output.append(LogLine.strip())  # Collect matching lines

# Print all at once to reduce print call overhead
print("\n".join(output))
