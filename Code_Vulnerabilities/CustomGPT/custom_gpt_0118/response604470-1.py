
import re

text = """
<p>Cash nbs $336,008</p>
<p>Total revenue $400,000</p>
<p>Cash value $13,000</p>
"""

# Regular expression pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Finding all matches
matches = re.findall(pattern, text)

# Process matches to extract desired output
for match in matches:
    cash_word = match[0]
    cash_amount = match[1] if match[1] else "N/A"  # If no amount, return "N/A"
    print(f"Found: {cash_word}, Amount: {cash_amount}")
