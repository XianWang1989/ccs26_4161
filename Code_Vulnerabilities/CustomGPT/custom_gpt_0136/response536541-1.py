
import re

# Read the log file
with open("file.txt") as log:
    log_lines = log.readlines()

# Prepare to store the results in a list
output_lines = []

# Process each log line
for log_line in log_lines:
    flag = True
    for key, conf_lines in Conf.items():
        for pattern in conf_lines:
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    if flag:
        output_lines.append(log_line.strip())

# Print all lines at once to reduce print calls
print("\n".join(output_lines))
