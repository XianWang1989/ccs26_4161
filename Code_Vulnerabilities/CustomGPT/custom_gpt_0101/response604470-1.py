
import re

text = """
<p>Cash nbs $13,000</p>
<p>Total: $336,008</p>
"""

pattern = r'<p>(.*?Cash.*?)(?:.*?(\$\d{1,3}(?:,\d{3})*))?</p>'

matches = re.findall(pattern, text)

for match in matches:
    cash_word = match[0]
    amount = match[1] if match[1] else "N/A"
    print(f"Cash Word: {cash_word}, Amount: {amount}")
