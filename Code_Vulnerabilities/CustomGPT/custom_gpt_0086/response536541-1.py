
import re
import sys

Log = open("file.txt")
output_lines = []

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
        # Collecting lines instead of printing immediately
        output_lines.append(LogLine.strip())

# Printing all at once to reduce output time
sys.stdout.write("\n".join(output_lines) + "\n")
