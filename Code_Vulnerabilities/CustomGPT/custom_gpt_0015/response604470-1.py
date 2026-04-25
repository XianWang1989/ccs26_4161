
import re

# Sample HTML input
html_text = """
<p>Cash nbs $336,008</p>
<p>Total revenue: $12,000</p>
<p>Cash flow: $13,000</p>
"""

# Regex pattern to match <p> tags containing "Cash" and optionally a number
pattern = r'<p>(.*?\bCash\b.*?)(?:.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?))?</p>'

matches = re.findall(pattern, html_text)

# Extracting and printing results
for match in matches:
    cash_text = match[0]  # The text containing "Cash"
    number = match[1] if match[1] else "No number found"  # The optional number
    print(f"Extracted: '{cash_text.strip()}', Number: '{number}'")
