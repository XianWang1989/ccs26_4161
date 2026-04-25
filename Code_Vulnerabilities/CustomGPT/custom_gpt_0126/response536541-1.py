
import re
from concurrent.futures import ThreadPoolExecutor

def check_line(log_line):
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

with open("file.txt") as log_file:
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(check_line, log_file))

for result in results:
    if result:
        print(result)
