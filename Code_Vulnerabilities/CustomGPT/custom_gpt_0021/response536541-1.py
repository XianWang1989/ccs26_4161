
import re

# Pre-compile your regex patterns 
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in ConfLine]
    for key, ConfLine in Conf.items()
}

# Open the log file
with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key in compiled_patterns:
            for pattern in compiled_patterns[key]:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(LogLine.strip())
