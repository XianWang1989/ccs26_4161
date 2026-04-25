
import re

string = "some large text here. This text contains some words and text."
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print the results
for sub_string, position in matches:
    print(f"{sub_string}: {position}")
