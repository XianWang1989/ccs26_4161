
import re

string = "some large text here"
sub_strings = ["some", "text", "notfound"]  # Example substrings

# Create a regex pattern to match any of the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

for match in matches:
    print(f"{match.group()} found at position {match.start()}")
