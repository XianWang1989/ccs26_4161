
import re

# Large string
string = "some large text here" * 10000  # Simulating a large string

# List of substrings
sub_strings = ["some", "text", "large", "missing"]

# Create a regex pattern from the list of substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all matches
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print results
for sub_string in sub_strings:
    if sub_string in matches:
        print(sub_string, matches[sub_string])
