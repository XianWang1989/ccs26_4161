
import re

# Example large string
string = "some large text here with some more text as examples"
# List of substrings
sub_strings = ["some", "text", "examples", "notfound"]

# Create a regular expression pattern by joining the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use re.finditer to find all occurrences of the pattern
matches = re.finditer(pattern, string)

# Print the found substrings and their positions
for match in matches:
    print(f"{match.group()} found at position {match.start()}")
