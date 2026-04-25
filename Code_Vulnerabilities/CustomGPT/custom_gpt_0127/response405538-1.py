
import re

# Larger string
string = "some large text here. some additional large text for testing purposes."

# List of substrings
sub_strings = ["some", "text", "large", "testing", "other"]

# Create a regex pattern to match any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match: [] for match in sub_strings}
for match in re.finditer(pattern, string):
    matches[match.group(0)].append(match.start())

# Print the results
for sub_string, positions in matches.items():
    if positions:
        for position in positions:
            print(f"'{sub_string}' found at position {position}")
