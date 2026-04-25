
import re

text = """
<p>Cash nbs $336,008</p>
<p>Some other content</p>
<p>Cash is important $13,000</p>
<p>Total earnings $5,000</p>
"""

# Define the regex pattern
pattern = r'<p>.*?\bCash\b.*?(?:\$(\d{1,3}(?:,\d{3})*))?</p>'

# Find all matches
matches = re.findall(pattern, text)

# Process and display results
results = []
for match in matches:
    cash_value = match[0] if match else None
    results.append("Cash" + (f" {cash_value}" if cash_value else ""))

# Output results
for result in results:
    print(result)
