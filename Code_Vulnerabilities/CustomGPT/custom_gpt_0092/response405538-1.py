
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to get matches and their positions
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print results
for sub in sub_strings:
    if sub in matches:
        print(sub, matches[sub])
