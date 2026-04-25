
import re

Log = open("file.txt")
results = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                flag = False
                break 
        if not flag:
            break 
    if flag:
        results.append(LogLine.strip())

# Print all results at once
print("\n".join(results))
