
import re

text = """
<p>Cash nbs $336,008</p>
<p>Total nbs $12,000</p>
"""

# The regex pattern
pattern = r'<p>(Cash.*?(\$\d{1,3}(?:,\d{3})*))?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and print results
for match in matches:
    cash_word = match[0].strip() if match[0] else None
    number = match[1] if match[1] else None
    print(f"Found: {cash_word}, Number: {number}")
