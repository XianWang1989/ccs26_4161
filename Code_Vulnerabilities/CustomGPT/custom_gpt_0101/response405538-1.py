
import re

string = "some large text here"  # Your large string
sub_strings = ["some", "text"]    # Your list of substrings

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches with their positions
matches = [(match.start(), match.group()) for match in re.finditer(pattern, string)]

for position, substring in matches:
    print(substring, position)
