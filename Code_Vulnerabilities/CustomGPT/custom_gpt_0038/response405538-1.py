
import re

# Large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text", "large", "notfound"]

# Compile regex pattern
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = {match.group(): match.start() for match in pattern.finditer(string)}

# Print results
for sub_string in sub_strings:
    if sub_string in matches:
        print(f"{sub_string} found at index {matches[sub_string]}")
    else:
        print(f"{sub_string} not found")
