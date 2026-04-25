
import re

Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        if not flag:
            break  # Exit early if we've already found a match
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.search(patterns, LogLine):  # Change to re.search if needed
                flag = False
                break 
    if flag:
        output_lines.append(LogLine.strip())

# Print all lines at once to minimize the time spent on print calls
print("\n".join(output_lines))

Log.close()
