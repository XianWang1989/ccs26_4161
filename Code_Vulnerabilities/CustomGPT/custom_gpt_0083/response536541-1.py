
import re

# Open the log file
with open("file.txt") as log:
    output_lines = []  # Buffer for storing lines to print

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
            output_lines.append(log_line.strip())  # Store the line instead of printing immediately

    # Print all lines at once
    print("\n".join(output_lines))
