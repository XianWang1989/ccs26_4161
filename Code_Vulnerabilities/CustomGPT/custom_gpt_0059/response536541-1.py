
import re
import concurrent.futures

Log = open("file.txt")
output_lines = []

def check_patterns(LogLine):
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            if re.match(DateString + pattern, LogLine):
                flag = False
                break
        if not flag:
            break
    return LogLine.strip() if flag else None

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(check_patterns, LogLine): LogLine for LogLine in Log}
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            output_lines.append(result)

# Print outputs at once (optional)
print("\n".join(output_lines))

Log.close()
