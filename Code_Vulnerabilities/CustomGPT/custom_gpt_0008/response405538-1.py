
import re

# Larger string
string = "some large text here, and some more text for testing purposes."
# List of substrings
sub_strings = ["some", "text", "large", "testing"]

# Create a regex pattern to match any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)
for match in matches:
    print(f"'{match.group()}' found at position {match.start()}")
