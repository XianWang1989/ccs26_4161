
import re

# Load your patterns from Conf
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}
Log = open("file.txt")

for LogLine in Log:
    if all(not any(pattern.search(LogLine) for pattern in compiled_patterns[key]) for key in compiled_patterns):
        # Print without waiting for a delay caused by other operations
        print(LogLine.strip())

Log.close()
