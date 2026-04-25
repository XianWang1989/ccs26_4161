
import re

string = "some large text here"
sub_strings = ["some", "text", "large", "hello", "world"]

# Create a regex pattern to match any of the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Use finditer to get positions of all matches
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print results
for sub_string in sub_strings:
    if sub_string in matches:
        print(sub_string, matches[sub_string])
