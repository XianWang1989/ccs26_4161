
import re

text = """
<p>Cash nbs $336,008 other text not needed</p>
<p>Cash other text $200,000</p>
<p>Total $400,000</p>
"""

# Regular expression to find "Cash" and an optional number
pattern = r'<p>(?:.*?\bCash\b.*?(\$\d{1,3}(?:,\d{3})*)?)<\/p>'

matches = re.findall(pattern, text)

# Printing found matches
for match in matches:
    cash_amount = match if match else 'No amount found'
    print(f'Extracted: Cash, Amount: {cash_amount}')
