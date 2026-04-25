
import re

# Sample large string
string = "some large text here, and some more text somewhere else."
# List of substrings to search for
sub_strings = ["some", "text"]

# Create a regex pattern by joining the substrings with '|'
pattern = '|'.join(map(re.escape, sub_strings))

# Use re.finditer to find all occurrences
matches = re.finditer(pattern, string)

# Print the positions of each substring found
for match in matches:
    print(match.group(0), match.start())
