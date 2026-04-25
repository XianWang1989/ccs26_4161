
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches of the pattern in the string
matches = [(m.group(0), m.start()) for m in re.finditer(pattern, string)]

# Print the results
for match in matches:
    print(match[0], match[1])
