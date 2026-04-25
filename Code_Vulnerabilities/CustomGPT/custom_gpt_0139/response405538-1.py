
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern from the substrings, escaping any special characters
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use re.finditer to find all matches of the pattern in the string
matches = re.finditer(pattern, string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
