
import re

# Compile your patterns outside the loop
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in conf_line]
    for key, conf_line in Conf.items()
}

with open("file.txt") as log:
    results = []
    for log_line in log:
        flag = True
        for key, patterns in compiled_patterns.items():
            if any(pattern.match(log_line) for pattern in patterns):
                flag = False
                break
        if flag:
            results.append(log_line.strip())

# Print all results at once
print("\n".join(results))
