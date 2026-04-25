
import re

# Define the large string and list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches in the string along with their positions
matches = [(match.start(), match.group(0)) for match in re.finditer(pattern, string)]

# Print the results
for position, substring in matches:
    print(f"'{substring}' found at position {position}")
