
import re

# Sample configuration dictionary for demonstration.
Conf = {
    'key1': ['pattern1', 'pattern2'],
    'key2': ['pattern3']
}

DateString = "2024-07-03 "  # Example date string
output_lines = []

with open("file.txt") as Log:
    for LogLine in Log:
        flag = True
        for key, ConfLine in Conf.items():
            for pattern in ConfLine:
                full_pattern = DateString + pattern
                if re.match(full_pattern, LogLine):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            output_lines.append(LogLine.strip())

# Print all results in one go
print("\n".join(output_lines))
