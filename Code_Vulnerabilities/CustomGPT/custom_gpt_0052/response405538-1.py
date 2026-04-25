
import re

# Define the large string and the list of substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches along with their positions
matches = [(m.group(), m.start()) for m in re.finditer(pattern, string)]

# Print the matches and their positions
for match, position in matches:
    print(f"{match}: {position}")
