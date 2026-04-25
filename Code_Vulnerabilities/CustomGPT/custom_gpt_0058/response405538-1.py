
import re

# Your large string
string = "some large text here"

# List of substrings to search for
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(re.escape(sub) for sub in sub_strings))

# Use finditer to find all matches and their positions
for match in pattern.finditer(string):
    print(match.group(), match.start())
