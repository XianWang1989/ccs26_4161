
import re

# You should define 'Conf' and 'DateString' accordingly
Conf = {
    # Example configuration
    'example_key': ['pattern1', 'pattern2']
}
DateString = "2023-07-03"  # Adjust as necessary

log_output = []  # Buffer for log output

with open("file.txt") as log_file:
    for log_line in log_file:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                patterns = DateString + pattern
                if re.match(patterns, log_line):
                    flag = False
                    break
            if not flag:
                break

        if flag:
            log_output.append(log_line.strip())

# Print all results at once
print("\n".join(log_output))
