
import re

# Load the log file
with open("file.txt") as log_file:
    log_lines = log_file.readlines()

# Create combined regex patterns from Conf
combined_patterns = []
for key, conf_lines in Conf.items():
    for pattern in conf_lines:
        combined_patterns.append(f"{DateString}{pattern}")

# Compile the regex pattern, joining all patterns with '|'
final_pattern = re.compile('|'.join(combined_patterns))

# Iterate through log lines and print matches
for log_line in log_lines:
    if not final_pattern.search(log_line):
        print(log_line.strip())
