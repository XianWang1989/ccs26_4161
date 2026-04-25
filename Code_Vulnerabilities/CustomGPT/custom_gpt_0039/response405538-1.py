
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all matches and their positions
matches = re.finditer(pattern, string)

# Print the matched substrings and their positions
for match in matches:
    print(match.group(), match.start())
