
import re

# Read the configuration into a more efficient format
Compilations = {key: [re.compile(DateString + pattern) for pattern in conf_line] for key, conf_line in Conf.items()}

# Read log file
with open("file.txt") as log_file:
    output = []  # Store lines to print later
    for log_line in log_file:
        flag = True
        for key, compiled_patterns in Compilations.items():
            for pattern in compiled_patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:  # If the flag is False, break out of the loop early
                break
        if flag:
            output.append(log_line.strip())

# Print all results at once for improved performance
print('\n'.join(output))
