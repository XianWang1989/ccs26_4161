
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches with their positions
matches = [(m.group(), m.start()) for m in re.finditer(pattern, string)]

# Print the results
for sub_string, position in matches:
    print(f"{sub_string}: {position}")
