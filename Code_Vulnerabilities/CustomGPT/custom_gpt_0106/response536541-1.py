
import re

# Open the log file
with open("file.txt") as log_file:
    results = []  # List to collect results
    for log_line in log_file:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                full_pattern = DateString + pattern
                if re.match(full_pattern, log_line):
                    flag = False
                    break  # Exit the innermost loop
            if not flag:
                break  # Exit the middle loop
        if flag:
            results.append(log_line.strip())  # Collect lines to print later

# Print all results at once
if results:
    print("\n".join(results))
