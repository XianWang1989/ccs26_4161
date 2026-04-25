
import re

text = """
<p>Cash nbs $336,008</p>
<p>Other content $13,000</p>
<p>Total $150,000</p>
"""

pattern = r'<p>\s*(Cash.*?)?\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?\s*</p>'

matches = re.findall(pattern, text)

for match in matches:
    cash = match[0].strip() if match[0] else None
    number = match[1]
    print(f'Cash: {cash}, Number: {number}')
