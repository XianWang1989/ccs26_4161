
import re
import threading
from queue import Queue

# Precompile regex patterns
patterns_dict = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

# Function to process logs and print
def process_logs(log_queue):
    while True:
        log_line = log_queue.get()
        if log_line is None:  # Check for termination condition
            break

        flag = True
        for key, patterns in patterns_dict.items():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(log_line.strip())
        log_queue.task_done()

# Create a queue and a thread for processing logs
log_queue = Queue()
thread = threading.Thread(target=process_logs, daemon=True)
thread.start()

# Read log file
with open("file.txt") as Log:
    for LogLine in Log:
        log_queue.put(LogLine)

# Wait for processing to complete and terminate the thread
log_queue.join()
log_queue.put(None)  # Signal the thread to terminate
