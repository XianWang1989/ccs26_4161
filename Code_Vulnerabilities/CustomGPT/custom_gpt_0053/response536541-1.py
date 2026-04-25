
import re

# Open log file
with open("file.txt") as log:
    output_lines = []  # Buffer to collect output lines
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
            output_lines.append(log_line.strip())  # Collect lines to output buffer

    # Print all collected lines at once
    if output_lines:
        print("\n".join(output_lines))
