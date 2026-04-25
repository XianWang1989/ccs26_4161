
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Other text without cash</p>
<p>Total $500,000</p>
<p>Cash amount $13,000</p>
"""

# Regular expression pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Print results
for match in matches:
    cash_word = match[0]      # This will be "Cash"
    amount = match[1] if match[1] else "No amount"  # Optional amount
    print(f"Found: {cash_word}, Amount: {amount}")
