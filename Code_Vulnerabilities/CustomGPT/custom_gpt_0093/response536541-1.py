
import re
from concurrent.futures import ThreadPoolExecutor

def process_log_line(log_line, patterns):
    for pattern in patterns:
        if re.match(pattern, log_line):
            return None  # Skip this log line
    return log_line.strip()  # Return log line if not skipped

Log = open("file.txt")
Conf = {
    # Sample patterns; replace with your actual configuration
    'example_key': [r'some_pattern', r'another_pattern']
}
DateString = "2024-07-04"  # Example date string

# Compile patterns for efficiency
compiled_patterns = [DateString + pattern for conf_lines in Conf.values() for pattern in conf_lines]

with ThreadPoolExecutor() as executor:
    results = list(executor.map(lambda line: process_log_line(line, compiled_patterns), Log))

for result in results:
    if result:
        print(result)

Log.close()
