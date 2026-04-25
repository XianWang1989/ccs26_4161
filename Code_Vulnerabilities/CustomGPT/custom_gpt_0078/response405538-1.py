
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use finditer to get all occurrences and their positions
matches = re.finditer(pattern, string)

for match in matches:
    print(match.group(), match.start())
