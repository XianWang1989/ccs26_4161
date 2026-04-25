
import re
from concurrent.futures import ThreadPoolExecutor

def check_log_line(log_line):
    flag = True
    for key, conf_line in Conf.items():
        for pattern in conf_line:
            combined_pattern = DateString + pattern
            if re.match(combined_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    return log_line.strip() if flag else None

with open("file.txt") as log_file:
    with ThreadPoolExecutor() as executor:
        results = executor.map(check_log_line, log_file)

for result in results:
    if result:
        print(result)
