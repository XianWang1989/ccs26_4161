
import re
import multiprocessing

def check_line(log_line, conf, date_string):
    flag = True
    for key, conf_line in conf.items():
        for pattern in conf_line:
            full_pattern = date_string + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    return log_line.strip() if flag else None

if __name__ == "__main__":
    # Configuration dictionary
    Conf = {
        # Sample patterns for demonstration
        "key1": [r'some_pattern1', r'some_pattern2'],
        "key2": [r'some_pattern3', r'some_pattern4']
    }

    DateString = "2023-07-02"  # Example date string

    with open("file.txt") as log:
        log_lines = log.readlines()

    # Use multiprocessing to speed up output
    with multiprocessing.Pool() as pool:
        results = pool.starmap(check_line, [(line, Conf, DateString) for line in log_lines])

    # Filter out None results
    for result in filter(None, results):
        print(result)
