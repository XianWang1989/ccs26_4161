
import re

# Sample input string with <p> tags
text = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Total profits are $336,008</p>
"""

# Regular expression to capture "Cash" and an optional number
pattern = r'<p>\s*(Cash.*?)\s*(?:\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Extracting and printing results
for match in matches:
    print(match.strip())
