
import re

string = "some large text here"
sub_strings = ["some", "text", "notfound", "large"]

# Create a regex pattern from the list of substrings
pattern = re.compile('|'.join(re.escape(sub) for sub in sub_strings))

# Find all matches in the larger string
matches = pattern.finditer(string)

# Print the substring and its position
for match in matches:
    print(match.group(), match.start())
