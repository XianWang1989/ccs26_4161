
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regular expression pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = re.finditer(pattern, string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
