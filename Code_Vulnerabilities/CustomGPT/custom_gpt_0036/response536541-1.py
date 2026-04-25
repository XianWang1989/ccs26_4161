
import re
from concurrent.futures import ThreadPoolExecutor

def process_line(log_line, conf, date_string):
    flag = True
    for key, conf_line in conf.items():
        for pattern in conf_line:
            patterns = date_string + pattern
            if re.match(patterns, log_line):
                flag = False
                break
        if not flag:
            break
    return log_line.strip() if flag else None

def main():
    conf = {
        # Example configuration; replace with your actual config
        'example_key': ['pattern1', 'pattern2']
    }
    date_string = '2023-03-14 '  # Example date string

    with open("file.txt") as log:
        log_lines = log.readlines()

    # Using ThreadPoolExecutor to process lines in parallel
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda line: process_line(line, conf, date_string), log_lines)

    # Filter out None results
    output_lines = [line for line in results if line is not None]

    # Print all lines at once
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
