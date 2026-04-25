
import re

# The large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text", "notfound"]

# Create a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

# Print the results
for match in matches:
    print(f"{match.group()} found at position {match.start()}")
