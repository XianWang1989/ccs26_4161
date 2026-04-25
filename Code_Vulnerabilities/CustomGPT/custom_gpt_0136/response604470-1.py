
import re

# Sample HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Total income $336,008</p>
"""

# Regex pattern to capture "Cash" and the number (if present)
pattern = r'<p>(.*?\bCash\b.*?)(\$[\d,]+)?</p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Extract and display the results
for match in matches:
    cash_text = match[0]  # Text containing "Cash"
    number = match[1] if match[1] else "No number present"  # The number, if available
    print(f"Captured: {cash_text.strip()} | Number: {number}")
