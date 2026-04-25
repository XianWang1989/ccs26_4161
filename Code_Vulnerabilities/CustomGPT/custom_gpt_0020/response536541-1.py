
import re
from concurrent.futures import ThreadPoolExecutor

def check_patterns(LogLine):
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:
            break 
    if flag:
        return LogLine.strip()
    return None

def print_results(result):
    if result is not None:  # Only print if the result is not None
        print(result)

DateString = "2023-10-01"  # Adjust according to your needs
Conf = {
    # Assuming Conf is a dictionary with patterns
    "example_key": ["error.*", "warning.*"]
}

# Reading the log file and processing the lines
with open("file.txt") as Log:
    with ThreadPoolExecutor() as executor:
        futures = []
        for LogLine in Log:
            futures.append(executor.submit(check_patterns, LogLine))

        for future in futures:
            result = future.result()  # This will block until the result is ready
            print_results(result)      # Call the print function with the result

