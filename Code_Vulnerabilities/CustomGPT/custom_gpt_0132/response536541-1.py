
import re

# Assuming Conf is defined somewhere in your code
Log = open("file.txt")
output_lines = []  # List to store output
DateString = "your_date_format"  # Define your date format

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        output_lines.append(LogLine.strip())  # Collecting output instead of printing immediately

# Print all output lines at once
print("\n".join(output_lines))
