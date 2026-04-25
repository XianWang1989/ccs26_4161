
import re

# Sample HTML input
html_content = """
<p>Cash nbs $13,000</p>
<p>Total $336,008</p>
<p>Cash something else $336,008</p>
"""

# Regex pattern to capture 'Cash' and optional dollar amount
pattern = r'<p>(.*?\bCash\b.*?)(?:\$([\d,]+))?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process matches
for match in matches:
    cash_text = match[0]
    dollar_amount = match[1] if match[1] else "not available"
    print(f"Found: '{cash_text.strip()}', Dollar Amount: '{dollar_amount}'")
