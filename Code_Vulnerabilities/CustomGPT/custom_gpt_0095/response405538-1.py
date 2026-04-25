
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = {match.group(0): match.start() for match in pattern.finditer(string)}

# Print the results
for sub, pos in matches.items():
    print(f"{sub}: {pos}")
