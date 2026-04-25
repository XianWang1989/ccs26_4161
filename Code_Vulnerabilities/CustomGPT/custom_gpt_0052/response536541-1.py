
import re
from multiprocessing import Pool

def check_log_line(log_line):
    flag = True
    for key, conf_lines in Conf.items():
        for pattern in conf_lines:
            full_pattern = DateString + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    return log_line.strip() if flag else None

if __name__ == "__main__":
    with open("file.txt") as log_file:
        log_lines = log_file.readlines()

    with Pool() as pool:
        results = pool.map(check_log_line, log_lines)

    # Filter out None values and print in one go
    filtered_results = filter(None, results)
    print("\n".join(filtered_results))
