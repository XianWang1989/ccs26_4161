
import re

# Large string
string = "some large text here with some other text included multiple times"
# List of substrings
sub_strings = ["some", "text", "other", "included", "not_present"]

# Create a regex pattern from the substrings
pattern = '|'.join(map(re.escape, sub_strings))
regex = re.compile(pattern)

# Find all matches and their positions
matches = regex.finditer(string)
for match in matches:
    print(match.group(), match.start())
