
import re

# Your large string
string = "some large text here that includes some text for testing"
# List of substrings
sub_strings = ["some", "text", "notfound"]

# Compile a regex pattern that matches any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)
for match in matches:
    print(f"'{match.group()}' found at position {match.start()}")
