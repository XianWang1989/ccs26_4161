
import re

# Assume Conf is your dictionary with patterns
Conf = {
    "key1": ["pattern1", "pattern2"],
    "key2": ["pattern3", "pattern4"],
}
DateString = "2023-03-01"  # Example date string

Log = open("file.txt")
output_lines = []  # List to store lines to print later

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

# Print all results at once
print("\n".join(output_lines))

# Close the log file
Log.close()
