
import re

# Sample input HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Some other content</p>
<p>Cash has some stuff I don't want then a number $336,008.</p>
<p>Total value is $250,000</p>
"""

# Regex to match content within <p> tags that starts with "Cash" and includes an optional dollar amount
pattern = r'<p>\s*(Cash.*?)\s*(\$[\d,]+)?\s*</p>'

# Finding all matches in the HTML content
matches = re.findall(pattern, html_content)

# Extracting only the relevant captures (Cash and its associated number)
results = [(match[0].strip(), match[1]) for match in matches if match[0].startswith('Cash')]

# Displaying the results
for cash_info in results:
    cash_value = cash_info[1] if cash_info[1] else "No amount"
    print(f"Extracted: {cash_info[0]}, Amount: {cash_value}")
