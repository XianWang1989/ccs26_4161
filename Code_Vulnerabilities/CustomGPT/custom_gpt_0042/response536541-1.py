
import re

# Assuming 'Conf' is defined earlier in your code and contains the patterns
Conf = {
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3']
}
DateString = '2024-07-03'  # Example date string

# Pre-compile regex patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

# Open log file
with open("file.txt") as log_file:
    results = []

    for log_line in log_file:
        flag = True
        for patterns in compiled_patterns.values():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break

        if flag:
            results.append(log_line.strip())

    # Print all results at once
    if results:
        print("\n".join(results))
