
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the list of substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = [(match.group(0), match.start()) for match in re.finditer(pattern, string)]

# Print results
for substring, position in matches:
    print(substring, position)
