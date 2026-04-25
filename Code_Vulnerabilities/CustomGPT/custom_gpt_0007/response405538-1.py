
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a single regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use finditer to get positions of all matches
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
