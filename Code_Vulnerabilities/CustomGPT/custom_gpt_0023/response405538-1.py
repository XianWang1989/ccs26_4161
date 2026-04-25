
import re

string = "some large text here"
sub_strings = ["some", "text", "large", "here", "notfound"]  # Example list of substrings

# Create a regular expression pattern for all substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches and their positions
matches = {match: m.start() for m in re.finditer(pattern, string) for match in [match.group()]}

for sub in sub_strings:
    if sub in matches:
        print(sub, matches[sub])
