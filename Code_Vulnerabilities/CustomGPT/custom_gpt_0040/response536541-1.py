
import re
import threading

Log = open("file.txt")

def print_line(line):
    print(line.strip())

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
        # Use threading to print without blocking
        threading.Thread(target=print_line, args=(LogLine,)).start()

Log.close()
