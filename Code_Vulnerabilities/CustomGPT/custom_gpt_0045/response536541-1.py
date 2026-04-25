
import re

# Assume Conf is defined somewhere in your script
Conf = {
    # Placeholder for your configuration dictionary
    # 'key': ['pattern1', 'pattern2', ...]
}

DateString = "2023-01-01"  # Example date string

# Open the log file
with open("file.txt") as Log:
    output_lines = []  # List to store the output results

    # Iterate through each line in the log file
    for LogLine in Log:
        flag = True
        for key, ConfLine in Conf.items():
            for patterns in ConfLine:
                patterns = DateString + patterns
                if re.match(patterns, LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            output_lines.append(LogLine.strip())  # Add to list instead of printing

# Print all results at once
print("\n".join(output_lines))  # Faster print output
