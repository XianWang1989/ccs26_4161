
import re

# Sample configuration dictionary
Conf = {
    'config1': ['pattern1', 'pattern2'],
    'config2': ['pattern3', 'pattern4']
}

DateString = "2024-07-03"  # Example date string
results = []

# Open and read the log file
with open("file.txt") as log_file:
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

# Output the results all at once
print("\n".join(results))
