
import re
from multiprocessing import Pool

# Function to process each log line
def process_line(LogLine):
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:
            return None
    return LogLine.strip() if flag else None

# Read log file
with open("file.txt") as Log:
    log_lines = Log.readlines()

# Create a pool of workers
with Pool() as pool:
    results = pool.map(process_line, log_lines)

# Filter out None values and print the results
for result in filter(None, results):
    print(result)
