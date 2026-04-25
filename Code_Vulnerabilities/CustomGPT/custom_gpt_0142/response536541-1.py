
import re

# Open the log file
Log = open("file.txt")
output_lines = []  # List to collect the output lines

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
        output_lines.append(LogLine.strip())  # Collect line for later output

# Print all collected lines at once
print("\n".join(output_lines))

# Don't forget to close the file
Log.close()
