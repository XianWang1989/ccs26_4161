
import re

# Your large string
string = "some large text here that contains some important text and more text"
# List of substrings to find
sub_strings = ["some", "text", "important"]

# Create a regex pattern from substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches in the string with their positions
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
