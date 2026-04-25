
import re

# Sample HTML string
html_content = """
<p>Cash nbs $13,000</p>
<p>Total sales $336,008</p>
<p>Cash Tips $336,008</p>
"""

# Regex pattern to match the desired content within <p> tags
pattern = r'<p>(.*?Cash.*?)(\$[,\d]+)?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Output the results
for match in matches:
    cash_text = match[0]  # The text that includes "Cash"
    amount = match[1] if match[1] else "No amount found"
    print(f"Cash Text: '{cash_text.strip()}', Amount: '{amount}'")
