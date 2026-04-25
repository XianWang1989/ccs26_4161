
import re

# Your large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches in the string
matches = pattern.finditer(string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
