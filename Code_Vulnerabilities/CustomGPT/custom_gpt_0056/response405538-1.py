
import re

# Sample large string
string = "some large text here, some more text here and some other text"
# List of substrings to find
sub_strings = ["some", "text", "large", "other", "notfound"]

# Create a regular expression pattern
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match: [] for match in sub_strings}
for match in re.finditer(pattern, string):
    matches[match.group()].append(match.start())

# Print results
for sub in sub_strings:
    if matches[sub]:
        print(sub, matches[sub])
