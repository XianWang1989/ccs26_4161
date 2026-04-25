
import re

# Open the log file and read lines
with open("file.txt") as log:
    output_lines = []
    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                # Prepend DateString to the pattern
                full_pattern = DateString + pattern
                if re.match(full_pattern, log_line):
                    flag = False
                    break
            if not flag:  # Break outer loop if a match is found
                break
        if flag:
            output_lines.append(log_line.strip())

# Print all output lines at once
print("\n".join(output_lines))
