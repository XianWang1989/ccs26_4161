
import re
import threading

def process_logs(log_file, conf):
    results = []

    with open(log_file) as Log:
        for LogLine in Log:
            flag = True
            for key, ConfLine in conf.items():
                for pattern in ConfLine:
                    pattern = DateString + pattern
                    if re.match(pattern, LogLine):
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                results.append(LogLine.strip())

    # Print results using a separate thread
    threading.Thread(target=print_results, args=(results,)).start()

def print_results(results):
    for line in results:
        print(line)

# Example usage
Conf = {
    'key1': ['pattern1', 'pattern2'],
    # Add more keys and patterns as needed
}
DateString = "2023-07-03_"  # Update with your date prefix
process_logs("file.txt", Conf)
