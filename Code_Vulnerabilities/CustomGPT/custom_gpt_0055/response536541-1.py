
import re

# Read the log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Prepare an output list
output_lines = []

# Process each line
for log_line in log_lines:
    flag = True
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            full_pattern = f"{DateString}{pattern}"
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break

    if flag:
        output_lines.append(log_line.strip())

# Print all results at once
if output_lines:
    print("\n".join(output_lines))
