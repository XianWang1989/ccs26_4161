
import re
from multiprocessing import Pool

# Read the configuration
Conf = {
    # Example of how the configuration might look
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3', 'pattern4']
}

# Prepare patterns by prefixing with DateString
DateString = "2023-07-01"  # Example date
patterns_dict = {key: [DateString + pattern for pattern in conf_lines] for key, conf_lines in Conf.items()}

def process_line(log_line):
    for key, patterns in patterns_dict.items():
        for pattern in patterns:
            if re.match(pattern, log_line):
                return None  # Skip this log line if it matches
    return log_line.strip()  # Return the log line if it does not match

if __name__ == "__main__":
    with open("file.txt") as log_file:
        log_lines = log_file.readlines()

    # Use multiprocessing to process lines
    with Pool() as pool:
        results = pool.map(process_line, log_lines)

    # Filter out None results and print the remaining log lines
    for result in filter(None, results):
        print(result)
