
import re
import threading

# Define a function to print log lines
def print_log(line):
    print(line.strip())

# Open the log file
with open("file.txt") as log:
    for log_line in log:
        flag = True
        for key, conf_line in Conf.items():
            for pattern in conf_line:
                pattern = DateString + pattern
                if re.match(pattern, log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            # Use threading to print the log line
            threading.Thread(target=print_log, args=(log_line,)).start()
