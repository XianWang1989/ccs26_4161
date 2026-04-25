
import re

# Define your large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all matches
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
