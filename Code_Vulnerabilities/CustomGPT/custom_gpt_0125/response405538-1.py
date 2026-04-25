
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regular expression pattern
pattern = '|'.join(map(re.escape, sub_strings))

# Find all occurrences of the substrings
matches = [(match.group(0), match.start()) for match in re.finditer(pattern, string)]

for substring, position in matches:
    print(substring, position)
