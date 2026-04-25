
import re

# Assumed sample list of regex patterns from the Config dictionary
Conf = {
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3']
}

# Precompile regex patterns
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in patterns] for key, patterns in Conf.items()}

# Open the log file and initialize a list to collect results
with open("file.txt") as Log:
    results = []
    for LogLine in Log:
        flag = True
        for key, compiled_conf_lines in compiled_patterns.items():
            for pattern in compiled_conf_lines:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(LogLine.strip())

# Print all results at once
print('\n'.join(results))
