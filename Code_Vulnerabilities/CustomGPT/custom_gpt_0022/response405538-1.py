
import re

# Large string
string = "some large text here, with other text and some more text"
# List of substrings
sub_strings = ["some", "text"]

# Create a regular expression pattern
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use re.finditer to find all occurrences of the pattern
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print results
for sub_str, position in matches:
    print(f"{sub_str}: {position}")
