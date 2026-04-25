
import re

# Read the log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Assuming Conf is predefined
# Create a set of patterns for faster lookup
patterns_set = {DateString + pattern for conf in Conf.values() for pattern in conf}

# Collect results
output_lines = []

for log_line in log_lines:
    flag = True
    for pattern in patterns_set:
        if re.match(pattern, log_line):
            flag = False
            break
    if flag:
        output_lines.append(log_line.strip())

# Print all results at once
print("\n".join(output_lines))
