
import re

Log = open("file.txt")
output_lines = []  # Buffer for output

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        # Create a combined pattern list for better efficiency
        combined_patterns = [DateString + pattern for pattern in ConfLine]

        # Use any() for faster matching
        if any(re.match(pattern, LogLine) for pattern in combined_patterns):
            flag = False
            break 

    if flag:
        output_lines.append(LogLine.strip())  # Collect lines to print later

# Print all lines at once
print("\n".join(output_lines))
