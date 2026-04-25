
import re

string = "some large text here. Some more text here."
sub_strings = ["some", "text", "large", "more"]

# Create a regex pattern from the substrings
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Function to find all matches and their positions
def find_substrings(s, pattern):
    positions = {}
    for match in pattern.finditer(s):
        positions[match.group()] = match.start()
    return positions

# Find the positions
positions = find_substrings(string, pattern)

# Print results
for substring, position in positions.items():
    print(substring, position)
