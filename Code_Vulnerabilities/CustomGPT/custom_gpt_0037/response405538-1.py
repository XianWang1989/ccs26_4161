
import re

string = "some large text here"
sub_strings = ["some", "text", "large", "here", "notfound"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = {match: match.start() for match in pattern.finditer(string)}

# Print the matches and their positions
for sub in sub_strings:
    if sub in matches:
        print(f"{sub}: {matches[sub]}")
