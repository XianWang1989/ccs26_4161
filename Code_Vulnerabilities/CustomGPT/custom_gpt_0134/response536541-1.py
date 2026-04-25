
import re

# Assuming Conf is a predefined dictionary and DateString is defined
Log = open("file.txt")
results = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            patterns = DateString + pattern
            if re.match(patterns, LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        results.append(LogLine.strip())

# Print all results at once
print("\n".join(results))

Log.close()
