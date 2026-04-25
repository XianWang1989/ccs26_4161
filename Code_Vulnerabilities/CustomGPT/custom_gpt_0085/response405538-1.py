
import re

# Define the large string
string = "some large text here, some more text here"

# List of substrings to find
sub_strings = ["some", "text"]

# Create a regex pattern that includes all substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use re.finditer to get matches for all substrings
matches = re.finditer(pattern, string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
