
import re

# Open the log file and read lines
with open("file.txt") as log:
    results = []
    for log_line in log:
        flag = True
        # Using a set for faster membership testing
        for key, conf_lines in Conf.items():
            combined_patterns = {DateString + pattern for pattern in conf_lines}
            if any(re.match(pattern, log_line) for pattern in combined_patterns):
                flag = False
                break
        if flag:
            results.append(log_line.strip())

# Print all results at once
print("\n".join(results))
