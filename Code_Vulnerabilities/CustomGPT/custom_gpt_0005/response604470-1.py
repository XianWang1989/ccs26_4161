
import re

text = """
<p>Cash nbs $336,008</p>
<p>Cash payment for services $13,000</p>
<p>Total revenue $100,000</p>
<p>No match here</p>
"""

pattern = r'<p>(.*?\bCash\b.*?(\$[\d,]+)?).*?</p>'
matches = re.findall(pattern, text)

for match in matches:
    cash_word = "Cash"
    number = match[1] if match[1] else None
    print(f"Found: {cash_word}, Amount: {number}")
