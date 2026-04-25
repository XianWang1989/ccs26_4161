
import re
from threading import Thread
from queue import Queue

def log_processor(log_queue, conf_patterns):
    while True:
        log_line = log_queue.get()
        if log_line is None:
            break
        flag = True
        for patterns in conf_patterns:
            pattern = DateString + patterns
            if re.match(pattern, log_line):
                flag = False
                break
        if flag:
            print(log_line.strip())
        log_queue.task_done()

# Load your configuration patterns
conf_patterns = [p for conf in Conf.values() for p in conf]

log_queue = Queue()
# Start a thread for processing logs
thread = Thread(target=log_processor, args=(log_queue, conf_patterns))
thread.start()

# Read the log file and enqueue lines for processing
with open("file.txt") as log_file:
    for log_line in log_file:
        log_queue.put(log_line)

# Stop the thread
log_queue.put(None)
thread.join()
