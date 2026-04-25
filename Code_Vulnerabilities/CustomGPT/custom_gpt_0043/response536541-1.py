
import re

# Assuming Conf is defined as a dictionary somewhere in your code
Conf = {
    'example_key': [r'some_pattern', r'another_pattern'],
}

# Precompile the patterns for efficiency
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in patterns] for key, patterns in Conf.items()}

# Open log file
with open("file.txt") as Log:
    output_lines = []  # Collect lines to print later
    for LogLine in Log:
        flag = True
        for key, comp_patterns in compiled_patterns.items():
            for pattern in comp_patterns:
                if pattern.match(LogLine):
                    flag = False
                    break  # Exit the innermost loop if a match is found
            if not flag:
                break  # Exit the second loop if a match is already found
        if flag:
            output_lines.append(LogLine.strip())  # Collect the line instead of printing immediately

# Now print all at once to reduce the time taken in output operation
if output_lines:  # Only print if there is something to print
    print("\n".join(output_lines))
