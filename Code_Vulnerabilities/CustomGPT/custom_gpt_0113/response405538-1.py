
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to find all matches in the string
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
