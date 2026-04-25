
import re
import threading

def process_log_line(log_line):
    flag = True
    for key, conf_line in Conf.items():
        for patterns in conf_line:
            patterns = DateString + patterns
            if re.match(patterns, log_line):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(log_line.strip())

def main():
    with open("file.txt") as log:
        threads = []
        for log_line in log:
            thread = threading.Thread(target=process_log_line, args=(log_line,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
