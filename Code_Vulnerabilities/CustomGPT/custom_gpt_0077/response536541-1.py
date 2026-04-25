
import re

# Open the log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Example configuration dictionary
Conf = {
    'some_key': [r'some_pattern1', r'some_pattern2']  # Add your actual patterns here
}

# Use a generator to yield matching lines
def find_matching_lines(log_lines, conf, date_string):
    for log_line in log_lines:
        line_matched = False
        for key, conf_lines in conf.items():
            for pattern in conf_lines:
                full_pattern = date_string + pattern
                if re.match(full_pattern, log_line):
                    line_matched = True
                    break
            if line_matched:
                break
        if not line_matched:
            yield log_line.strip()

# Date string placeholder
date_string = "2023-07-01 "  # Adjust appropriately

# Print all results at once
print("\n".join(find_matching_lines(log_lines, Conf, date_string)))
