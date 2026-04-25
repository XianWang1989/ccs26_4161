
import re

def find_substring_positions(string, sub_strings):
    # Create a single regex pattern that matches any of the substrings
    pattern = '|'.join(map(re.escape, sub_strings))
    matches = re.finditer(pattern, string)

    # Collect and print positions of found substrings
    positions = {match.group(): match.start() for match in matches}
    return positions

# Example usage
string = "some large text here"
sub_strings = ["some", "text"]
positions = find_substring_positions(string, sub_strings)

for sub_str, pos in positions.items():
    print(f"Substring '{sub_str}' found at position {pos}")
