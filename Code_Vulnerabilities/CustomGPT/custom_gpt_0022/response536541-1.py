
import re

# Open the log file
with open("file.txt") as log_file:
    results = []  # List to store results

    for log_line in log_file:
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
            results.append(log_line.strip())  # Collect result

# Print all results once
print('\n'.join(results))
