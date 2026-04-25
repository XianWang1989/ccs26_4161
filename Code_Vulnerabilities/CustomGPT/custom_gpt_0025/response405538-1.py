
import re

# Sample data
string = "some large text here, with some text included"
sub_strings = ["some", "text", "included"]

# Create a regex pattern
pattern = "|".join(map(re.escape, sub_strings))

# Find all matches and their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Print results
for substring, position in matches:
    print(f"{substring} found at position {position}")
