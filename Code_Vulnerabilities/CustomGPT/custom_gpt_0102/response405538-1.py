
import re

# Large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text", "large", "example"]

# Create a regex pattern that matches any of the substrings
pattern = "|".join(map(re.escape, sub_strings))

# Find all matches with their positions
matches = {m.start(): m.group() for m in re.finditer(pattern, string)}

# Print results
for position, substring in matches.items():
    print(f"Substring '{substring}' found at position {position}")
