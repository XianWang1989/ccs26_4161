
import re

Log = open("file.txt")
output_lines = []  # Create a list to store the lines to be printed

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:  # No need to check further if the flag is already False
            break

    if flag:
        output_lines.append(LogLine.strip())  # Append the line to the list instead of printing

# Print all collected lines at once
print("\n".join(output_lines))

Log.close()  # Don't forget to close the file
