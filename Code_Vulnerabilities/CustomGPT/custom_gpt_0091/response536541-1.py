
import re

# Sample configuration dictionary
Conf = {
    'example_key': ['pattern1', 'pattern2'],
}

# Assume DateString is defined
DateString = "2023-07-03"

# Open the log file
with open("file.txt") as log_file:
    output_lines = []

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
            output_lines.append(log_line.strip())

# Print all results at once
print("\n".join(output_lines))
