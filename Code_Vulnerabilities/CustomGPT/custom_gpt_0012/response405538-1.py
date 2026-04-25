
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches
matches = {m.start(): m.group(0) for m in re.finditer(pattern, string)}

# Print the positions and substrings
for position, substring in matches.items():
    print(substring, position)
