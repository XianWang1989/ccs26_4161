
import re

# Open log file
with open("file.txt") as log:
    # Precompile patterns
    compiled_patterns = {}
    for key, ConfLine in Conf.items():
        compiled_patterns[key] = [re.compile(DateString + pattern) for pattern in ConfLine]

    results = []
    for log_line in log:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(log_line):
                    flag = False
                    break
            if not flag:
                break

        if flag:
            results.append(log_line.strip())

    # Print all results at once
    print("\n".join(results))
