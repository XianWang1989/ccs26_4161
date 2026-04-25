
import re

# Initialize an empty list to store results
results = []

with open("file.txt") as log:
    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                combined_pattern = DateString + pattern
                if re.match(combined_pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(log_line.strip())

# Print all results at once
print("\n".join(results))
