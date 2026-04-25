
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to get the positions of all matches
matches = re.finditer(pattern, string)

# Print the results
for match in matches:
    print(match.group(), match.start())
