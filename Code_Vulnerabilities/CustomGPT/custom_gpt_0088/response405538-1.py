
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print matches
for match in matches:
    print(match[0], match[1])
