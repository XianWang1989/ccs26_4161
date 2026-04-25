
import re

text = """
<p>Cash nbs $336,008</p>
<p>Total amount: $1,000</p>
<p>Some irrelevant text</p>
"""

pattern = r'<p>(?=.*\bCash\b)(.*?)\$(\d{1,3}(?:,\d{3})*)<\/p>'
matches = re.findall(pattern, text)

for match in matches:
    print(f"Extracted: 'Cash', Amount: ${match[1]}")
