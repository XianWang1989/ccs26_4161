
import re

# Open the log file
with open("file.txt") as log_file:
    results = []
    for log_line in log_file:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                pattern = DateString + pattern
                if re.match(pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(log_line.strip())

# Print all results at once
print("\n".join(results))
