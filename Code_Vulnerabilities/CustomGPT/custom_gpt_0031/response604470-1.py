
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008</p>
<p>Cash nbs $13,000</p>
<p>Not required text</p>
"""

# Regex pattern
pattern = r'<p>(?=.*\bCash\b)(.*?\bCash\b.*?)(?:(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?))?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Extracting "Cash" and the number
results = [(match[0], match[1]) for match in matches]
for cash, amount in results:
    print(f'Found: "{cash.strip()}", Amount: "{amount if amount else 'None'}"')
