
import re

def find_substrings_positions(main_string, sub_strings):
    # Create a regex pattern that captures all substrings
    pattern = '|'.join(map(re.escape, sub_strings))

    # Use re.finditer to find all occurrences of the pattern
    matches = re.finditer(pattern, main_string)

    # Collect results
    positions = {}
    for match in matches:
        positions[match.group()] = match.start()

    return positions

# Example usage
main_string = "some large text here, some other text here"
sub_strings = ["some", "text", "other"]

positions = find_substrings_positions(main_string, sub_strings)
for substring, position in positions.items():
    print(f"'{substring}' found at position {position}")
