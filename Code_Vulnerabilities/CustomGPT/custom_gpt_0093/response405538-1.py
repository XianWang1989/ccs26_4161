
import re

# Large string
string = "some large text here with some more text and other characters"
# List of substrings
sub_strings = ["some", "text", "large", "not_in_string"]

# Join substrings into a regex pattern
pattern = r'|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match.group(0): match.start() for match in re.finditer(pattern, string)}

# Print the results
for substring in sub_strings:
    if substring in matches:
        print(substring, matches[substring])
