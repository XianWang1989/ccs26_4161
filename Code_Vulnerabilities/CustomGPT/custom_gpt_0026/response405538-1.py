
import re

string = "some large text here, some small text there"
sub_strings = ["some", "text"]

# Create a regex pattern for all substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Use finditer to get all matches and their positions
matches = {m.group(): m.start() for m in re.finditer(pattern, string)}

# Print results
for sub_string in sub_strings:
    if sub_string in matches:
        print(f"{sub_string}: {matches[sub_string]}")
