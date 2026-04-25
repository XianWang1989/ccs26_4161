
import re

Log = open("file.txt")
results = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:  # Early exit if flag is false
            break 
    if flag:
        results.append(LogLine.strip())  # Collecting results instead of printing immediately

# Print all results at once
print("\n".join(results))

Log.close()
