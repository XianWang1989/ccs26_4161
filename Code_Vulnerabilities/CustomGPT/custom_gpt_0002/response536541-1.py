
import re

def read_log(file_path):
    with open(file_path) as log:
        for line in log:
            yield line.strip()

log_generator = read_log("file.txt")
for log_line in log_generator:
    flag = True
    for key, conf_line in Conf.items():
        patterns = [DateString + pattern for pattern in conf_line]
        if any(re.match(pattern, log_line) for pattern in patterns):
            flag = False
            break 
    if flag:
        print(log_line)
