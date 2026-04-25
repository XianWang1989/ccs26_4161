
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total expenses: $336,008</p>
<p>Cash transaction: $336,008</p>
<p>No cash info here.</p>
<p>Cash: $300</p>
"""

# Using regex to search for <p>... </p> and capture required information
pattern = r'<p>(.*?)</p>'

matches = re.findall(pattern, html_content)

# Extract "Cash" and the optional number
result = []
for match in matches:
    cash_match = re.search(r'\bCash\b.*?(\$\d{1,3}(?:,\d{3})*)?', match)
    if cash_match:
        # Cash and number (if it exists)
        result.append((cash_match.group(0), cash_match.group(1)))

# Display results
for cash_info, amount in result:
    if amount:
        print(f"Found: '{cash_info}' with amount: '{amount}'")
    else:
        print(f"Found: '{cash_info}' with no amount")
