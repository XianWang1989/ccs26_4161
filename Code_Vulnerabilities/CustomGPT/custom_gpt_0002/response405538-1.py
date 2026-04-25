
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a single regex pattern from all substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches in the larger string
matches = pattern.finditer(string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
