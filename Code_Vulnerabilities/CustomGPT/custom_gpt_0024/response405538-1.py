
import re

def find_substrings_positions(main_string, sub_strings):
    # Create a regex pattern that matches any of the substrings.
    pattern = '|'.join(re.escape(sub) for sub in sub_strings)

    # Use re.finditer to find all matches and their positions
    matches = re.finditer(pattern, main_string)

    # Store results in a list
    positions = {match.group(): match.start() for match in matches}

    return positions

# Example usage
main_string = "some large text here, some more text here"
sub_strings = ["some", "text"]

positions = find_substrings_positions(main_string, sub_strings)

for substring, position in positions.items():
    print(f"{substring}: {position}")
