
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)
regex = re.compile(pattern)

# Find all matches and their positions
matches = regex.finditer(string)

for match in matches:
    print(f"{match.group()} found at index {match.start()}")
