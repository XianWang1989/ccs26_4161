
import re

# Large string
string = "some large text here"
# List of substrings to search for
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = "|".join(map(re.escape, sub_strings))
matches = re.finditer(pattern, string)

# Collect positions and substrings found
for match in matches:
    print(match.group(), match.start())
