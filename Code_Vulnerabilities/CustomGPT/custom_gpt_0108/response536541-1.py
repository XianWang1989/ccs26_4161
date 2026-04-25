
import re

# Read the log file
Log = open("file.txt")
results = []

# Iterate through each log line
for LogLine in Log:
    flag = True
    # Iterate through the configuration dictionary
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break
        if not flag:  # Exit early if a match was found
            break
    if flag:
        results.append(LogLine.strip())

# Print all results at once
print("\n".join(results))

# Close the log file
Log.close()
