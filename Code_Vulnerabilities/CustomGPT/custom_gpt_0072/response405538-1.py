
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use finditer to locate all matches and their positions
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

for sub in sub_strings:
    if sub in matches:
        print(f"{sub}: {matches[sub]}")
