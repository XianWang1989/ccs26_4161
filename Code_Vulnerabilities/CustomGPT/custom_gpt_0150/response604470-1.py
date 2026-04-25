
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total revenues: $336,008</p>
<p>Other content</p>
"""

# Regex pattern to match "Cash" and an optional number
pattern = r'<p>(.*?Cash.*?)\s*(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and print results
for match in matches:
    cash_text = match[0]
    amount = match[1] if match[1] else "No amount"
    print(f'Found: "{cash_text.strip()}", Amount: "{amount}"')
