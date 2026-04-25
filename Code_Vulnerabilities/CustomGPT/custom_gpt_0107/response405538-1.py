
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all occurrences of the substrings
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
