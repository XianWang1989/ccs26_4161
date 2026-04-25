
import re

Log = open("file.txt")
for LogLine in Log:
    if all(not re.match(DateString + pattern, LogLine) for key, ConfLine in Conf.items() for pattern in ConfLine):
        print(LogLine.strip())
