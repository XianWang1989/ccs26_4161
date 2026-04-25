
import re

string = "some large text here"
sub_strings = ["some", "text", "large", "missing"]

# Compile a regular expression pattern that matches any substring
pattern = re.compile('|'.join(map(re.escape, sub_strings)))

# Find all matches and their positions
matches = pattern.finditer(string)

for match in matches:
    print(match.group(), match.start())
