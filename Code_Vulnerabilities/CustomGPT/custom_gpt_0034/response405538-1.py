
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to get all matches along with their positions
matches = re.finditer(pattern, string)

for match in matches:
    print(match.group(), match.start())
