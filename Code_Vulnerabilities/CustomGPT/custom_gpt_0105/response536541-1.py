
import re

# Open the log file
Log = open("file.txt")

# Initialize a list to store results
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break
        if not flag:  # Exit early if a match is found
            break
    if flag:
        output_lines.append(LogLine.strip())  # Append the result to the list

# Print all results at once
print("\n".join(output_lines))

# Always close the file after processing
Log.close()
