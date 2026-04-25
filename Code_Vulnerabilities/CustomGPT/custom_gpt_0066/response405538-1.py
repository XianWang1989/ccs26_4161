
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(re.escape(s) for s in sub_strings)

# Find all matches with their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print the results
for substr, position in matches:
    print(substr, position)
