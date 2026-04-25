
import re

text = """
<p>Cash nbs $336,008</p>
<p>Cash nbs</p>
<p>Total $13,000</p>
"""

# Regular expression definition
pattern = r'<p>(.*?\bCash\b.*?)(?:\$(\d{1,3}(?:,\d{3})*))?</p>'

matches = re.findall(pattern, text)

# Process matches to extract desired values
for match in matches:
    cash_part = match[0].strip()
    number_part = match[1] if match[1] else None
    print(f'Cash Part: {cash_part}, Number: {number_part}')
