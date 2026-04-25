
import re

# Open the log file and read lines
with open("file.txt") as log:
    results = []  # Create a list to hold results
    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                # Prepend DateString to the pattern
                full_pattern = DateString + pattern
                if re.match(full_pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(log_line.strip())  # Store result instead of printing immediately

# Print all results at once
print("\n".join(results))
