
import re

text = """
<p>Cash nbs $336,008</p>
<p>Total revenue $25,000</p>
<p>Cash $13,000</p>
<p>No cash here</p>
"""

# Regular expression pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Print results
for match in matches:
    cash_word, amount = match
    print(f"Found: {cash_word}, Amount: {amount if amount else 'None'}")
