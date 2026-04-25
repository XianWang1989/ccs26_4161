
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))
matches = re.finditer(pattern, string)

# Print the substring and its position
for match in matches:
    print(match.group(0), match.start())
