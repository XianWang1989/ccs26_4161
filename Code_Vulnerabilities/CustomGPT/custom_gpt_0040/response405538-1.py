
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Join substrings into a single regex pattern
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches with their positions
matches = [(match.group(0), match.start()) for match in re.finditer(pattern, string)]

# Print results
for sub_string, position in matches:
    print(f"'{sub_string}' found at position {position}")
