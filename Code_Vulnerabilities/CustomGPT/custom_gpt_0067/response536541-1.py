
import re

# Open the log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

results = []  # Store results here

# Iterate through the log lines
for log_line in log_lines:
    flag = True
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    if flag:
        results.append(log_line.strip())  # Collect results

# Print all results at once
print("\n".join(results))
