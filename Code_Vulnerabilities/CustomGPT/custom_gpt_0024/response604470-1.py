
import re

# Sample string input
text = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Cash has $336,008</p>
<p>Total: $100,000</p>
"""

# Regex pattern to find "Cash" and an optional dollar amount
pattern = r'<p>\s*(Cash)\s.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process matches to extract desired data
results = [(match[0], match[1]) for match in matches]

# Print results
for cash, amount in results:
    print(f'Found: "{cash}"', f'Amount: "{amount}"' if amount else 'No amount found')
