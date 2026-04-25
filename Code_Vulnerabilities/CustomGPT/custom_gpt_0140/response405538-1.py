
import re

# Large string
string = "some large text here and some more text to check"
# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches with their positions
matches = [(m.group(), m.start()) for m in re.finditer(pattern, string)]

# Print the results
for match in matches:
    print(match[0], match[1])
