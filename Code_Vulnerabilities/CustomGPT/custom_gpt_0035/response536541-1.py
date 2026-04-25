
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
        if not flag:
            break
    if flag:
        results.append(LogLine.strip())

# Print all results at once
print('\n'.join(results))
