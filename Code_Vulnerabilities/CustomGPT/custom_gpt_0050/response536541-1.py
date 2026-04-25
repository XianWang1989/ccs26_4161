
import re

# Precompile the patterns outside the loop for efficiency
compiled_patterns = [re.compile(DateString + pattern) for ConfLine in Conf.values() for pattern in ConfLine]

with open("file.txt") as Log:
    for LogLine in Log:
        # Check if any compiled pattern matches the LogLine
        if any(pattern.match(LogLine) for pattern in compiled_patterns):
            continue  # Skip this line if it matches any pattern
        print(LogLine.strip())
