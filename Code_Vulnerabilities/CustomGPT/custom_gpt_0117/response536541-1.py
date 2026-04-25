
import re
from threading import Thread
import queue

def process_logs(log_file, conf, output_queue):
    with open(log_file) as log:
        for log_line in log:
            flag = True
            for key, conf_lines in conf.items():
                for pattern in conf_lines:
                    pattern_full = DateString + pattern
                    if re.match(pattern_full, log_line):
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                output_queue.put(log_line.strip())

def print_output(output_queue):
    while True:
        line = output_queue.get()
        if line is None:  # Exit condition
            break
        print(line)

# Your configuration dictionary
Conf = {
    # example patterns
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3', 'pattern4']
}

DateString = "2024-07-01 "  # example date prefix
output_queue = queue.Queue()

# Start a thread for printing output
thread = Thread(target=print_output, args=(output_queue,))
thread.start()

# Process logs
process_logs("file.txt", Conf, output_queue)

# Signal the print thread to exit
output_queue.put(None)
thread.join()
