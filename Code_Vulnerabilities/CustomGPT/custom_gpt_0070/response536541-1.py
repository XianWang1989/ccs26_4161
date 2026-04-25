
import re

# Function to process the log file
def process_logs(log_file, conf):
    results = []

    # Read log file
    with open(log_file) as log:
        for log_line in log:
            flag = True
            for key, conf_lines in conf.items():
                for pattern in conf_lines:
                    pattern = DateString + pattern
                    if re.match(pattern, log_line):
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                results.append(log_line.strip())

    # Print all results at once
    print("\n".join(results))

# Example usage
if __name__ == "__main__":
    Conf = {
        'key1': ['pattern1', 'pattern2'],
        'key2': ['pattern3', 'pattern4']
    }
    DateString = "2023-07-01"
    process_logs("file.txt", Conf)
