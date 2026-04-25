
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the list of substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print the results
for sub_string, position in matches:
    print(sub_string, position)
