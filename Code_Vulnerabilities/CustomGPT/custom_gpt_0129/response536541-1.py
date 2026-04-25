
import re

# Precompile the regex patterns for better performance
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

def filter_logs(log_file, compiled_patterns):
    with open(log_file) as log:
        for log_line in log:
            flag = True
            for key, patterns in compiled_patterns.items():
                for pattern in patterns:
                    if pattern.match(log_line):
                        flag = False
                        break  # Exit the innermost loop if a match is found
                if not flag:
                    break  # Exit the second loop if a match was found
            if flag:  # If no matches were found, print the log line
                yield log_line.strip()  # Use a generator to yield each result

# Use the function to process the log file
for result in filter_logs("file.txt", compiled_patterns):
    print(result)
