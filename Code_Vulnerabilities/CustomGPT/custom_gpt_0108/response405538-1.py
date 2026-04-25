
import re

# Define your large string and list of substrings
string = "some large text here with some additional text for testing"
sub_strings = ["some", "text", "notfound"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their start positions
matches = {match: match.start() for match in re.finditer(pattern, string)}

# Print results
for sub in sub_strings:
    if sub in matches:
        print(f"'{sub}' found at position {matches[sub]}")
    else:
        print(f"'{sub}' not found")
