
import re

# Open the log file
with open("file.txt") as Log:
    results = []  # Collect results here
    for LogLine in Log:
        flag = True
        for key, ConfLine in Conf.items():
            for pattern in ConfLine:
                complete_pattern = DateString + pattern
                if re.match(complete_pattern, LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            results.append(LogLine.strip())  # Store result instead of printing

# Print all results at once
for result in results:
    print(result)
