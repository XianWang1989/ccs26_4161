
import re
import threading

output_lock = threading.Lock()

def async_print(line):
    with output_lock:
        print(line.strip())

comp_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}
Log = open("file.txt")

for LogLine in Log:
    if all(not any(pattern.search(LogLine) for pattern in comp_patterns[key]) for key in comp_patterns):
        thread = threading.Thread(target=async_print, args=(LogLine,))
        thread.start()

Log.close()
