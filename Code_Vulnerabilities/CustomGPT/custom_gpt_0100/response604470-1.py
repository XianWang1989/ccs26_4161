
import re

# Sample input
text = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>\s*(Cash.*?)?(\$[\d,]+)?\s*</p>"

# Searching with regex
match = re.search(pattern, text)

if match:
    cash = match.group(1) if match.group(1) else "Not found"
    amount = match.group(2) if match.group(2) else "Not found"
    print(f"Extracted: {cash}, Amount: {amount}")
else:
    print("No match found")
