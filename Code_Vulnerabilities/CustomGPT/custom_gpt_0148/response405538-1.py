
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print the substring and its position
for substring, position in matches:
    print(substring, position)
