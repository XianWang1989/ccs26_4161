
import re

# Sample HTML content
text = """
<p>Cash nbs $13,000</p>
<p>Total sales $336,008</p>
<p>Cash $336,008</p>
<p>Some other text</p>
"""

# Regular expression to match "Cash" and the optional number
pattern = r'<p>\s*(Cash)\s*.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, text)

# Print the results
for match in matches:
    cash_word = match[0]  # Always "Cash"
    number = match[1] if match[1] else "none"
    print(f'Found: "{cash_word}" with number: "{number}"')
