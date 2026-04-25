
import re

# Large string
string = "some large text here" * 10000  # Example large string
sub_strings = ["some", "text", "large"]  # Example substrings

# Create a regex pattern from the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Finding all matches along with their positions
matches = {match.group(): match.start() for match in re.finditer(pattern, string)}

# Print results
for sub in sub_strings:
    if sub in matches:
        print(f"{sub} found at position {matches[sub]}")
