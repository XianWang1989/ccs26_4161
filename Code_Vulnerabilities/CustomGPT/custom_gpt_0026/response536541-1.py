
import re

# Assuming Conf is your dictionary and DateString is defined
Log = open("file.txt")
pattern_set = {DateString + pattern for ConfLine in Conf.values() for pattern in ConfLine}

for LogLine in Log:
    flag = True
    for pattern in pattern_set:
        if re.match(pattern, LogLine):
            flag = False
            break
    if flag:
        print(LogLine.strip())

Log.close()
