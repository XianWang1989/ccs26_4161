
import re

text = """
<p>Cash nbs $336,008</p>
<p>Total can be $12,000</p>
<p>Just text here</p>
"""

# Regex to find "Cash" and an optional number
pattern = r'<p>(?P<keyword>Cash).*?(?P<number>\$\d{1,3}(?:,\d{3})*)?</p>'

matches = re.finditer(pattern, text)

for match in matches:
    keyword = match.group('keyword')
    number = match.group('number') if match.group('number') else "Not found"
    print(f"Keyword: {keyword}, Number: {number}")
