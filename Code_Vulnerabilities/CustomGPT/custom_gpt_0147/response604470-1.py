
import re

# Sample input string
input_string = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>(.*?Cash.*?)((?:.*?\$[\d,]+)?)(<\/p>)'

# Search using the regex
match = re.search(pattern, input_string)

# Check if a match was found
if match:
    cash = "Cash" if "Cash" in match.group(1) else None
    number = match.group(2).strip() if match.group(2).strip() else None
    print(f"Extracted cash word: {cash}")
    print(f"Extracted number (if available): {number}")
else:
    print("No match found.")
