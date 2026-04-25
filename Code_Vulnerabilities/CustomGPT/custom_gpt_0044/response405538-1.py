
import re

string = "some large text here, and some more text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = r'|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all occurrences
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
