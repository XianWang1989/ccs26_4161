
import re
import sys

Log = open("file.txt")
output_lines = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        # Combine patterns into a single regex for efficiency
        combined_pattern = '|'.join([DateString + pattern for pattern in ConfLine])
        if re.search(combined_pattern, LogLine):
            flag = False
            break

    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once for better performance
print("\n".join(output_lines))
sys.stdout.flush()
