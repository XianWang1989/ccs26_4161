
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regular expression pattern from the list of substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)
matches = {match.start(): match.group() for match in re.finditer(pattern, string)}

# Print results
for position, substring in matches.items():
    print(f"{substring} found at position {position}")
