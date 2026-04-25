
import re
import threading

# Example configuration dictionary
Conf = {
    "pattern1": ["error", "warning"],
    "pattern2": ["info", "debug"]
}

Log = open("file.txt")

# Function to process and print matching lines
def process_log_line(log_line):
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            # Construct the full pattern with DateString if necessary
            # DateString is assumed to be defined somewhere in your code
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break 
        if flag == False:
            break 
    if flag:
        print(log_line.strip())

# Read and process each line in the log file
threads = []
for LogLine in Log:
    thread = threading.Thread(target=process_log_line, args=(LogLine,))
    threads.append(thread)
    thread.start()  # Start the thread for each log line

# Wait for all threads to complete
for thread in threads:
    thread.join()

Log.close()
