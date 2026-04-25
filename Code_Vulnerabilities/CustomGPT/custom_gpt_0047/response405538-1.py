
import re

# Define the large string and substrings
string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern by joining the substrings
pattern = '|'.join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print the results
for sub in sub_strings:
    if sub in matches:
        print(f"{sub}: {matches[sub]}")
