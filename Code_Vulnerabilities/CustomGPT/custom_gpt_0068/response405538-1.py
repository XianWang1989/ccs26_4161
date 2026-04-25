
import re

# Define the large string and the list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Compile the substrings into a single regex pattern
# The | character acts as an OR operator in regex
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

# Print the found substrings and their positions
for match in matches:
    print(f"{match.group(0)} found at position {match.start()}")
