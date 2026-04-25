
import re
import threading

def print_log_line(log_line):
    print(log_line.strip())

Log = open("file.txt")
threads = []

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
        thread = threading.Thread(target=print_log_line, args=(LogLine,))
        thread.start()
        threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

Log.close()
