
import re

# Sample text
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r'<p>\s*(Cash.*?)?\$?([\d,]+)?\s*</p>'

# Find matches
matches = re.findall(pattern, text)

# Extracting results
for match in matches:
    cash = match[0].strip() if match[0] else None
    number = match[1] if match[1] else None

    print(f"Cash: {cash}, Number: {number}")
