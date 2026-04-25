
import re

# Sample text containing <p> tags.
text = """
<p>Cash nbs $13,000</p>
<p>Total $336,008</p>
<p>Something else</p>
<p>Cash $336,008</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Print results
for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else "No amount"
    print(f"Found: {cash_word}, Amount: {amount}")
