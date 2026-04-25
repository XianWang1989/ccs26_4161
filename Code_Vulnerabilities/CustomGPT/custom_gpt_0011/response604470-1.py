
import re

# Sample text containing <p> tags
text = "<p>Cash nbs $13,000</p><p>Total revenue $336,008</p>"

# Regex pattern to match "Cash" and an optional number
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d{1,3}(?:,\d{3})*(?:\.\d{2})?]?)?\s*</p>'

# Finding all matches
matches = re.findall(pattern, text)

# Printing the extracted results
for match in matches:
    cash, amount = match
    print(f"Extracted: '{cash}'", f"Amount: '{amount}'" if amount else "Amount: None")
