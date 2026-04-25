
import re

# Define the large string
string = "some large text here, some more text here"
sub_strings = ["some", "text"]

# Create a pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches with their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print the results
for substring, position in matches:
    print(substring, position)
