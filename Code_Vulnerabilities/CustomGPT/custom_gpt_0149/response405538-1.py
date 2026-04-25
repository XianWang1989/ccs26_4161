
import re

# Large string
string = "some large text here. some more text here."

# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern that looks for any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches and their positions
for match in re.finditer(pattern, string):
    print(match.group(), match.start())
