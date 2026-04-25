
import re

# Sample HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Cash some text $336,008</p>
"""

# Regex pattern to search for 'Cash' and capture the number
pattern = r'<p>(.*?\bCash\b.*?)\s*(\$[\d,]+)?<\/p>'

# Find all matches
matches = re.findall(pattern, html_content)

# Process and print results
for match in matches:
    cash_text = match[0].strip()
    amount = match[1] if match[1] else "No amount found"
    print(f"Extracted: '{cash_text}', Amount: '{amount}'")
