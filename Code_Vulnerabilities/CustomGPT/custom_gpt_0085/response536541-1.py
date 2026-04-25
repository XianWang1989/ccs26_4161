
import re
import multiprocessing

def process_log_line(log_line):
    flag = True
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break 
        if not flag:
            break 
    return log_line.strip() if flag else None

if __name__ == "__main__":
    with open("file.txt") as log:
        with multiprocessing.Pool() as pool:
            results = pool.map(process_log_line, log)

    for result in results:
        if result:
            print(result)
