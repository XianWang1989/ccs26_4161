
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the list of substrings
pattern = '|'.join(map(re.escape, sub_strings))
matches = re.finditer(pattern, string)

for match in matches:
    print(match.group(0), match.start())
