
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a regex pattern that matches any of the substrings
pattern = '|'.join(re.escape(sub) for sub in sub_strings)
matches = re.finditer(pattern, string)

# Loop through matches and print the position and the substring
for match in matches:
    print(f"{match.group(0)} found at index {match.start()}")

