
import re

# Sample input string
text = """
<p>Cash nbs $13,000</p>
<p>Total something $336,008</p>
<p>Cash and more stuff $336,008</p>
"""

# Outer regex to match <p> tags, with inner regex for extracting cash and number
pattern = r'<p>(.*?)<\/p>'

# Find all paragraphs
matches = re.findall(pattern, text)

# Inner regex to extract the desired components
inner_pattern = r'(Cash).*?(\$\d{1,3}(?:,\d{3})*)?'

for match in matches:
    inner_match = re.search(inner_pattern, match)
    if inner_match:
        cash_word = inner_match.group(1)
        number = inner_match.group(2)
        print(f'Found: {cash_word}', f'Number: {number if number else "N/A"}')
