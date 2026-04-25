
import re

# Sample HTML content
content = """
<p>Cash nbs $13,000</p>
<p>Total cash available $336,008</p>
<p>Some irrelevant text</p>
"""

# Regular expression to match <p> content and look for "Cash" and a possible number
pattern = r'<p>(.*?Cash.*?)(?:.*?(\$\d{1,3}(?:,\d{3})*))?.*?</p>'

# Find all matches in the content
matches = re.findall(pattern, content)

# Process results
for match in matches:
    cash_text = match[0]
    number = match[1] if match[1] else "No number found"
    print(f'Found: "{cash_text}", Number: "{number}"')
