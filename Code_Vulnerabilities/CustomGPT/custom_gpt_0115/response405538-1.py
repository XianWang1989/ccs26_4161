
import re

string = "some large text here"
sub_strings = ["some", "text"]

# Create a combined regex pattern
pattern = '|'.join(re.escape(sub) for sub in sub_strings)

# Find all matches in the string along with their positions
matches = [(match.group(), match.start()) for match in re.finditer(pattern, string)]

# Display the results
for substring, position in matches:
    print(substring, position)
