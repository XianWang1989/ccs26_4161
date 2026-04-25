
import re

# Load the log file
with open("file.txt") as log_file:
    results = []  # Store results here
    for log_line in log_file:
        flag = True
        for key, conf_lines in Conf.items():
            for pattern in conf_lines:
                # Prepend date string to the pattern
                full_pattern = f"{DateString}{pattern}"
                if re.match(full_pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(log_line.strip())  # Collect matching lines

# Print all results at once
print('\n'.join(results))
