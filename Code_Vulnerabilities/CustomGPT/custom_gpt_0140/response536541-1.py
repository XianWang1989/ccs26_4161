
import re
import sys

# Open the log file
with open("file.txt") as log:
    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                # Combine date string with the pattern
                full_pattern = DateString + pattern
                if re.match(full_pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            sys.stdout.write(log_line.strip() + '\n')
