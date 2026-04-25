
import re

# Sample HTML content
html_content = """
<p>Cash some unwanted text $336,008</p>
<p>Other text</p>
<p>Total $13,000</p>
"""

# Regex pattern to match <p> tags and capture "Cash" and the number if available
pattern = r'<p>\s*(Cash)\s*.*?(\$[\d,]+)?\s*</p>'

# Find all matches in the HTML content
matches = re.findall(pattern, html_content)

# Processing the matches
for match in matches:
    cash_word = match[0]  # This will be "Cash"
    number = match[1] if match[1] else "No number found"  # This might be empty
    print(f"Found: {cash_word}, Amount: {number}")
