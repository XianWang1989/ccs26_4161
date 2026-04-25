
import re

# Sample HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Total amount is $336,008</p>
<p>Something else</p>
"""

# Regex pattern
pattern = r'<p>(.*?\bCash\b.*?)(?:.*?(\$\d{1,3}(?:,\d{3})*))?</p>'

# Find matches
matches = re.findall(pattern, html_content)

# Extract results
results = [(match[0], match[1]) for match in matches]

# Print results
for cash, amount in results:
    print(f"Found: '{cash.strip()}' with amount: '{amount if amount else 'None'}'")
