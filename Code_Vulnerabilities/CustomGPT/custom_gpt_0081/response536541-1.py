
import re

# Load log file and patterns
Log = open("file.txt")
# It's assumed that Conf is your dictionary containing patterns
# Conf = {'key1': ['pattern1', 'pattern2'], 'key2': ['pattern3', 'pattern4']}

# Compile all patterns in advance
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in patterns] 
                     for key, patterns in Conf.items()}

results = []

for LogLine in Log:
    # Assume flag starts as True, if a match is found it will be set to False
    flag = True
    for key, compiled_patterns_list in compiled_patterns.items():
        # Check all patterns for the current line
        if any(pattern.match(LogLine) for pattern in compiled_patterns_list):
            flag = False
            break # Exit if one match is found
    if flag:
        results.append(LogLine.strip())

# Print all results at once
print("\n".join(results))

# Don't forget to close the log file
Log.close()
