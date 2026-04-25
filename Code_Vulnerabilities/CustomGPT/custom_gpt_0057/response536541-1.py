
import re
import threading

def process_log_line(log_line):
    flag = True
    for key, conf_lines in Conf.items():
        if not any(re.match(DateString + pattern, log_line) for pattern in conf_lines):
            flag = False
            break
    if flag:
        print(log_line.strip())

def main():
    with open("file.txt") as log_file:
        threads = []
        for log_line in log_file:
            thread = threading.Thread(target=process_log_line, args=(log_line,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    DateString = "YOUR_DATE_STRING_HERE"  # Set your date string
    Conf = {
        # Your dictionary configuration
    }
    main()
