
import re

string = "some large text here"
sub_strings = ["some", "text", "large", "notfound"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their starting positions
matches = {match: match.start() for match in re.finditer(pattern, string)}

# Print the results
for sub_string in sub_strings:
    if sub_string in matches:
        print(f"{sub_string}: {matches[sub_string]}")
    else:
        print(f"{sub_string}: Not found")
