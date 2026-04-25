
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {m.start(): m.group() for m in re.finditer(pattern, string)}

for position, substring in matches.items():
    print(substring, position)
