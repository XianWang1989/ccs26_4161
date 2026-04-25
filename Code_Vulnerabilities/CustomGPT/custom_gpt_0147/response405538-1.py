
import re

# Define the large string and the list of substrings
string = "some large text here"
substrings = ["some", "text", "large", "notfound"]

# Create a regex pattern from the substrings
pattern = '|'.join(map(re.escape, substrings))  # Escape special characters
regex = re.compile(pattern)

# Find all matches in the string
matches = regex.finditer(string)

# Print each match and its position
for match in matches:
    print(match.group(), match.start())
