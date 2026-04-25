
import re

text = """
<p>Cash nbs $336,008</p>
<p>Some other text</p>
<p>Cash nbs</p>
<p>Total: $500,000</p>
"""

pattern = r'<p>(.*?\bCash\b.*?)(?:\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?))?<\/p>'

matches = re.findall(pattern, text)

for match in matches:
    cash_text = match[0]
    dollar_amount = match[1] if match[1] else "No amount"
    print(f"Extracted: {cash_text.strip()}, Amount: {dollar_amount}")
