
import re

# Assuming Conf is defined somewhere above this snippet with patterns
# Conf = { ... }  # Example: {'key1': ['.*pattern1.*', '.*pattern2.*'], ...}
DateString = '2023-03-15 '  # Example Date String

# Open the log file and prepare to collect output
with open("file.txt") as Log:
    output = []  # List to accumulate results
    compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in conf_lines] 
                          for key, conf_lines in Conf.items()}

    for LogLine in Log:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:  # If we found a match, no need to continue checking
                break
        if flag:
            output.append(LogLine.strip())  # Accumulate the output instead of printing immediately

# Print all outputs at once to reduce I/O operation time
if output:
    print('\n'.join(output))
