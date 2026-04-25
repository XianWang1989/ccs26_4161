
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches
matches = re.finditer(pattern, string)

# Print the positions of each substring found
for match in matches:
    print(match.group(), match.start())
