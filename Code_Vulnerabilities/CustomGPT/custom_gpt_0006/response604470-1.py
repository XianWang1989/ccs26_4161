
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008</p>
<p>Total revenue: $500,000</p>
<p>Cash on hand $13,000</p>
"""

# Regular expression pattern
pattern = r"<p>\s*(Cash.*?)?(\$[\d,]+)?\s*</p>"

# Find all matches
matches = re.findall(pattern, html_content)

# Process and print results
for match in matches:
    cash_word = match[0] or "Cash not found"
    number = match[1] or "Number not found"
    print(f"Extracted: {cash_word.strip()}, Amount: {number}")
