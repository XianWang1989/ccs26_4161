
import re
import threading
import queue

def read_log(log_file, conf):
    output_queue = queue.Queue()

    def output_worker():
        while True:
            line = output_queue.get()
            if line is None:  # Check for shutdown signal
                break
            print(line.strip())

    # Start the output thread
    thread = threading.Thread(target=output_worker)
    thread.start()

    with open(log_file) as log:
        for log_line in log:
            flag = True
            for key, conf_line in conf.items():
                for pattern in conf_line:
                    full_pattern = DateString + pattern
                    if re.match(full_pattern, log_line):
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                output_queue.put(log_line)

    output_queue.put(None)  # Signal the thread to exit
    thread.join()  # Wait for the thread to finish

# Example call to the function
Conf = {
    # Your configuration dictionary
}
DateString = "2023-07-03 "  # Example date prefix
read_log("file.txt", Conf)
