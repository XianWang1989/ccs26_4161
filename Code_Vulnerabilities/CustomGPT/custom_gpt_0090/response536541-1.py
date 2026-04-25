
import re

with open("file.txt") as log_file:
    results = []  # List to store matching log lines
    for log_line in log_file:
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
            results.append(log_line.strip())

# Print all results at once
print("\n".join(results))
