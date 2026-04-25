
import re

# Compile the regex patterns once instead of in a loop
compiled_patterns = {
    key: [re.compile(DateString + pattern) for pattern in ConfLine]
    for key, ConfLine in Conf.items()
}

with open("file.txt") as log_file:
    # Read lines and filter them based on the compiled patterns
    results = []

    for log_line in log_file:
        if all(not any(pattern.match(log_line) for pattern in patterns) for patterns in compiled_patterns.values()):
            results.append(log_line.strip())

# Print results all at once, reducing print calls
print("\n".join(results))
