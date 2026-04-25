
import re

# Example HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Cash nbs $336,008</p>
"""

# Regular expression pattern
pattern = r'<p>\s*Cash.*?(\$[\d,]+)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Extract and print results
for match in matches:
    cash_amount = match[0] if match else None
    print(f'Found: Cash and amount: {cash_amount}')
