
import re
import sys

# Open the log file
Log = open("file.txt")
output = []

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
        output.append(LogLine.strip())

# Print all results at once to reduce print overhead
sys.stdout.write("\n".join(output) + "\n")

Log.close()
