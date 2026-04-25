
import re

# Assuming Conf is a predefined dictionary and DateString is a string
Log = open("file.txt")
output_lines = []  # Create a list to store the output

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
        output_lines.append(LogLine.strip())  # Add lines to the list instead of printing

Log.close()  # Don't forget to close the file

# Print all the collected output at once
if output_lines:
    print("\n".join(output_lines))
