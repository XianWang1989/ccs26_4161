
import re

# Sample input string
text = """
<p>Cash nbs $336,008</p>
<p>Other content</p>
<p>Another line Cash $13,000</p>
"""

# Regex pattern
pattern = r'<p>(Cash).*?(\$\d{1,3}(?:,\d{3})*)?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process matches to show results
for match in matches:
    cash_word = match[0]  # 'Cash'
    dollar_amount = match[1] if match[1] else "No amount found"
    print(f'Found "{cash_word}" with amount: {dollar_amount}')
