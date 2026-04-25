
import re

# Define your large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Create a pattern using the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches with their positions
for match in re.finditer(pattern, string):
    print(f"{match.group()} found at position {match.start()}")
