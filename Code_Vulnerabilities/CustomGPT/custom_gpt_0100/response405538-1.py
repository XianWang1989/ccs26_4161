
import re

string = "some large text here with some more text to check for some substrings"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

for sub, pos in matches:
    print(f"{sub}: {pos}")
