
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008</p>
<p>Other text $12,000</p>
<p>CASH irrelevant $13,000</p>
"""

# Regular expression to find "Cash" and the optional number
pattern = r'(?i)<p>\s*Cash.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Extract and format results
results = []
for match in matches:
    cash_found = "Cash"
    number_found = match if match else "N/A"
    results.append((cash_found, number_found))

# Output results
for cash, number in results:
    print(f"Found: {cash} with amount: {number}")
