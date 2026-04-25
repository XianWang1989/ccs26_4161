
import re

# Large string
string = "some large text here, some more text here, and even more text"

# List of substrings
sub_strings = ["some", "text", "more", "even"]

# Create a single regex pattern from the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches in the string
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print results
for sub_string, position in matches:
    print(f"Substring: '{sub_string}' found at position: {position}")
