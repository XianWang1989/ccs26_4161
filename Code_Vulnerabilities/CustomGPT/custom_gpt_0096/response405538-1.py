
import re

# Large string
string = "some large text here"

# List of substrings
sub_strings = ["some", "text"]

# Create a regex pattern to match any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches with their positions
matches = [(m.group(), m.start()) for m in re.finditer(pattern, string)]

# Print the results
for substring, position in matches:
    print(f"{substring} found at position {position}")
