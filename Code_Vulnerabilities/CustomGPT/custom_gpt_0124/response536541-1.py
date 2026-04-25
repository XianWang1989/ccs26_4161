
import re

# Open the log file
with open("file.txt") as log:
    results = []  # Accumulate results here
    for log_line in log:
        flag = True
        for key, conf_lines in Conf.items():
            # Check each pattern in the configuration line
            for pattern in conf_lines:
                combined_pattern = DateString + pattern
                if re.match(combined_pattern, log_line):
                    flag = False
                    break  # Exit inner loop if a match is found
            if not flag:
                break  # Exit outer loop if a match is found
        if flag:
            results.append(log_line.strip())  # Store the result

# Print all results at once
print("\n".join(results))
