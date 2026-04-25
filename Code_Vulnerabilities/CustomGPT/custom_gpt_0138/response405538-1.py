
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in pattern.finditer(string)]

for sub_string, position in matches:
    print(sub_string, position)
