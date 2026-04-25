
import re

# Assume Conf is a dictionary where keys are some identifiers and values are lists of patterns.
Conf = {
    'example_key': ['pattern1', 'pattern2'],
    'another_key': ['pattern3', 'pattern4']
}

# Compile the patterns into a single regex for efficiency
compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

# Create a list to store the results to print later
output_lines = []

with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key, patterns in compiled_patterns.items():
            for pattern in patterns:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:  # Exit the outer loop if a match is found
                break
        if flag:
            output_lines.append(LogLine.strip())

# Print the results at once for better performance
if output_lines:
    print("\n".join(output_lines))
