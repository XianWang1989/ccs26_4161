
import re

# Open the log file
with open("file.txt") as log:
    output_lines = []  # List to store output

    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                pattern = DateString + pattern
                if re.match(pattern, log_line):
                    flag = False
                    break
            if not flag:
                break

        if flag:
            output_lines.append(log_line.strip())  # Collect the line

    # Print all at once to reduce delay
    print("\n".join(output_lines))  # Print results in one go
