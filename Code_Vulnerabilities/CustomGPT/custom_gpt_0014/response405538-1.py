
import re

# Large string
string = "some large text here with some more text included"
# List of substrings
sub_strings = ["some", "text"]

# Join the substrings into a regex pattern
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print the results
for sub_string, position in matches.items():
    print(f'{sub_string} found at position {position}')
