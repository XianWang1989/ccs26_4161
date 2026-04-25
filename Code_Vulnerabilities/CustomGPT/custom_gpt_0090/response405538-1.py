
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern for the substrings
pattern = '|'.join(map(re.escape, sub_strings))
matches = re.finditer(pattern, string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
