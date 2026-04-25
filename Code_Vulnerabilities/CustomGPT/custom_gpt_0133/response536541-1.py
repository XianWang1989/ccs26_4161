
import re

# Open the log file
Log = open("file.txt")
output_lines = []

# Compile all patterns once.
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

for LogLine in Log:
    flag = True
    for patterns in compiled_patterns.values():
        for pattern in patterns:
            if pattern.match(LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        output_lines.append(LogLine.strip())

# Print all results at once
print('\n'.join(output_lines))

Log.close()
