
import re

# Assuming Conf is predefined as a dictionary containing patterns.
Conf = {
    'example_key': ['pattern1', 'pattern2'],  # This should be your actual patterns
}
DateString = '2022-11-'

# Open the log file
with open("file.txt") as Log:
    output_lines = []  # List to collect output lines
    # Compile regex patterns for efficiency
    compiled_patterns = {key: [re.compile(DateString + pattern) for pattern in ConfLine] for key, ConfLine in Conf.items()}

    for LogLine in Log:
        flag = True
        # Check against all previously compiled patterns
        for patterns in compiled_patterns.values():
            for pattern in patterns:
                if pattern.match(LogLine):
                    flag = False
                    break
            if not flag:
                break

        if flag:
            output_lines.append(LogLine.strip())

    # Print all gathered lines at once
    if output_lines:
        print("\n".join(output_lines))
