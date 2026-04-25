
import re

Log = open("file.txt")
output_lines = []  # List to hold the lines to be printed

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:  # Simplified check
            break 
    if flag:
        output_lines.append(LogLine.strip())  # Add line to list if flag is true

# Print all output lines at once
print("\n".join(output_lines))

Log.close()  # Remember to close the file after processing
