
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches and their start positions
matches = [(match.group(0), match.start()) for match in re.finditer(pattern, string)]

# Print the results
for sub_string, position in matches:
    print(sub_string, position)
