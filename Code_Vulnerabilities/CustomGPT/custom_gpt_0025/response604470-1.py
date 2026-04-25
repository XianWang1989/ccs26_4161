
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008</p>
<p>Total $12,000</p>
<p>Cash nbs</p>
"""

# Regular expression to extract "Cash" and an optional dollar amount
pattern = r'<p>.*?(Cash).*?(?:\$(\d{1,3}(?:,\d{3})*))?.*?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process matches
results = []
for match in matches:
    cash_word = match[0]  # "Cash"
    amount = match[1] if match[1] else "None"
    results.append((cash_word, amount))

# Display results
print(results)
