
import re

# Open the log file
with open("file.txt") as log_file:
    # Precompile the patterns for faster matching
    compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in conf_lines]
                         for key, conf_lines in Conf.items()}

    output_lines = []

    # Process each line in the log
    for log_line in log_file:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            output_lines.append(log_line.strip())

    # Print all results at once
    print("\n".join(output_lines))
