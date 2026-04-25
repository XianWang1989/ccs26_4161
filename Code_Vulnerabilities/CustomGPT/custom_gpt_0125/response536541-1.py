
import re

# Open the log file
Log = open("file.txt")
output_lines = []  # List to collect output lines

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
        output_lines.append(LogLine.strip())  # Collect the output instead of printing

# Print all collected output at once
print('\n'.join(output_lines))

Log.close()  # Don't forget to close the log file
