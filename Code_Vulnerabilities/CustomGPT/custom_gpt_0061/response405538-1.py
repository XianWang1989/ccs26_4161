
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches along with their positions
matches = [(m.group(0), m.start()) for m in pattern.finditer(string)]

for substring, position in matches:
    print(substring, position)
