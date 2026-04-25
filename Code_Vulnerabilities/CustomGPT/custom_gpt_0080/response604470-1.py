
import re

text = """
<p>Cash nbs $336,008</p>
<p>Other text here</p>
<p>Cash nbs $13,000</p>
"""

pattern = r"<p>.*?(Cash).*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?.*?</p>"
matches = re.findall(pattern, text)

for match in matches:
    cash_word = match[0]  # "Cash"
    amount = match[1] if match[1] else 'N/A'  # Amount or "N/A"
    print(f'Found: {cash_word}, Amount: {amount}')
