import re

# Compile regex patterns to speed up matching
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

# Open the log file and collect lines to print later
with open("file.txt") as Log:
    result_lines = []
    for LogLine in Log:
        flag = True
        for key, ConfLine in compiled_patterns.items():
            for pattern in ConfLine:
                if pattern.search(LogLine):  # Use .search() instead of re.match
                    flag = False
                    break
            if not flag:
                break
        if flag:
            result_lines.append(LogLine.strip())

# Print all collected lines at once
if result_lines:
    print("\n".join(result_lines))
