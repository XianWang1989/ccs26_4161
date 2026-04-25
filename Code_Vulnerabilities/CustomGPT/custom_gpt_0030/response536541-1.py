
import re

# Open the log file and initialize an output list
Log = open("file.txt")
output_lines = []

# Process each line in the log
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
        output_lines.append(LogLine.strip())

# Print all results at once to reduce the number of print calls
print("\n".join(output_lines))

# Close the log file
Log.close()
