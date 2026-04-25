
import re
import sys

# Assuming Conf is defined elsewhere
Log = open("file.txt")
output_buffer = []

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            patterns = DateString + pattern
            if re.match(patterns, LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        output_buffer.append(LogLine.strip())

# Flush output after processing all lines
sys.stdout.write("\n".join(output_buffer) + "\n")
