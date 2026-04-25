
import re

# Open the log file and prepare for output
with open("file.txt") as log:
    results = []
    for log_line in log:
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

# Print all results at once to speed up output
print("\n".join(results))
