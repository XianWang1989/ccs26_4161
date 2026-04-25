
import re
import threading

def process_logs(log_lines, conf, date_string):
    results = []  # Accumulate results here
    for log_line in log_lines:
        flag = True
        for key, conf_line in conf.items():
            for patterns in conf_line:
                patterns = date_string + patterns
                if re.match(patterns, log_line):
                    flag = False
                    break 
            if not flag:
                break 
        if flag:
            results.append(log_line.strip())

    # Print all results at once
    print('\n'.join(results))

def main():
    Log = open("file.txt")
    conf = {
        # Your configuration dictionary goes here
    }
    date_string = "2023-10-01"  # Example date string

    # Create a thread to process logs
    log_thread = threading.Thread(target=process_logs, args=(Log, conf, date_string))
    log_thread.start()
    log_thread.join()  # Wait for the thread to finish

if __name__ == "__main__":
    main()
