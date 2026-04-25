
import re

text = """
<p>Cash nbs $336,008</p>
<p>Some other text</p>
<p>Cash amount $13,000</p>
<p>Total</p>
"""

pattern = r'<p>\s*(Cash.*?)\s*(?:\$([\d,]+))?\s*</p>'
matches = re.findall(pattern, text)

for match in matches:
    cash_text = match[0]  # "Cash" and the following text if available
    amount = match[1] if match[1] else "No amount"  # Extract the amount or default message
    print(f"Text: {cash_text.strip()}, Amount: {amount}")
