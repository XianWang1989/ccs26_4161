
import re

def find_substrings_positions(string, sub_strings):
    # Create a regex pattern with non-capturing groups
    pattern = r'|'.join(map(re.escape, sub_strings))

    # Use finditer to get positions of each match
    matches = re.finditer(pattern, string)

    positions = {}
    for match in matches:
        positions[match.group()] = match.start()

    return positions

# Sample data
string = "some large text here with some text"
sub_strings = ["some", "text"]

positions = find_substrings_positions(string, sub_strings)
for sub in sub_strings:
    if sub in positions:
        print(f"{sub} found at position {positions[sub]}")
