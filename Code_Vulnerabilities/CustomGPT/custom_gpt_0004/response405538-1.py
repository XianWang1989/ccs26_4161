
import re

string = "some large text here, some more text for testing"
sub_strings = ["some", "text"]

# Create a single pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all matches and their positions
matches = re.finditer(pattern, string)

# Print each substring with its start position
for match in matches:
    print(f"{match.group()} found at position {match.start()}")
