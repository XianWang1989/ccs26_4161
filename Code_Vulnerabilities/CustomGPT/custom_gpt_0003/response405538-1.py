
import re

# Your large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern by joining all substrings with '|'
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all matches
matches = re.finditer(pattern, string)

# Print each match's position
for match in matches:
    print(match.group(), match.start())
