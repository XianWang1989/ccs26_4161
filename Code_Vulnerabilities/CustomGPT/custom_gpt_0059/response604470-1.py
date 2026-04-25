
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total revenue $336,008</p>
<p>Some other text</p>
"""

# Regex pattern
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*(\.\d{2})?)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process and display results
results = [(match[0], match[1]) for match in matches]
print(results)
