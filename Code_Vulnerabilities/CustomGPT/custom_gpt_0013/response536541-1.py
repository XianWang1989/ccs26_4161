
import re

# Open the log file
Log = open("file.txt")

# To store results
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            # Construct the full pattern
            full_pattern = DateString + patterns
            if re.match(full_pattern, LogLine):
                flag = False
                break 
        if not flag:
            break 
    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once
print("\n".join(output_lines))

# Close the log file
Log.close()
