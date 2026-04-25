
import re
import threading

# Open the log file
with open("file.txt") as log:
    log_lines = log.readlines()

# Function to process each log line and print if it matches
def process_log_line(log_line):
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
        print(log_line.strip())

# Create threads for each log line
threads = []
for log_line in log_lines:
    thread = threading.Thread(target=process_log_line, args=(log_line,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
