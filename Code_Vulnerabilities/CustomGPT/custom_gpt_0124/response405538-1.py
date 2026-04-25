
import re

# Large string
string = "some large text here with various words and some more text"

# List of substrings
sub_strings = ["some", "text", "large", "words"]

# Create a pattern from the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match: string.index(match) for match in re.findall(pattern, string)}

# Print results
for sub_string in matches:
    print(f"{sub_string}: {matches[sub_string]}")
