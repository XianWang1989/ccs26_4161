
import re

# Sample text
text = """
<p>Cash nbs $336,008</p>
<p>Total $1,000</p>
"""

# Regex pattern
pattern = r"<p>\s*(Cash)\s*(?:.*?)(\$\d{1,3}(?:,\d{3})*)?\s*</p>"

# Find all matches
matches = re.findall(pattern, text)

# Process matches
for match in matches:
    cash_word, amount = match
    print(f"Found: {cash_word}, Amount: {amount if amount else 'None'}")
