
import re
import threading

Log = open("file.txt")
output = []
lock = threading.Lock()

def print_output():
    global output
    while True:
        with lock:
            if output:
                print(output.pop(0).strip())
            else:
                break

printer_thread = threading.Thread(target=print_output)
printer_thread.start()

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
        with lock:
            output.append(LogLine)

# Wait for the printer thread to finish
printer_thread.join()
