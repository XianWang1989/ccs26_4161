
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a single regex pattern for all substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print results
for substring, position in matches:
    print(f"{substring} found at position {position}")
