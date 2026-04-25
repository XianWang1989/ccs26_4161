
import re

# Open the log file
with open("file.txt") as Log:
    results = []  # Collect results in a list

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
            results.append(LogLine.strip())  # Append to results instead of printing

# Print all results at once
if results:
    print("\n".join(results))
