
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern with all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to search for all matches
matches = re.finditer(pattern, string)

# Output the substring and its position
for match in matches:
    print(match.group(), match.start())
