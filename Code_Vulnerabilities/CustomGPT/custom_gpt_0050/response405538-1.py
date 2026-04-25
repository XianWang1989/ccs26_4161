
import re

# Your large string
string = "some large text here with some more text in it"
# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

# Print each substring and its position
for match in matches:
    print(f"{match.group()} found at {match.start()}")
