
import re

# Open the log file
with open("file.txt") as Log:
    results = []  # List to store matching lines

    for LogLine in Log:
        flag = True
        for key, ConfLine in Conf.items():
            for patterns in ConfLine:
                full_pattern = DateString + patterns
                if re.match(full_pattern, LogLine):
                    flag = False
                    break
            if not flag:  # Break out of outer loop if a match was found
                break

        if flag:
            results.append(LogLine.strip())

    # Print all results at once
    print("\n".join(results))
