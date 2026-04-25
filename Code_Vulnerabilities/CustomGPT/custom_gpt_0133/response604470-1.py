
import re

# Sample HTML content
html_content = """
<p>Cash nbs $13,000</p>
<p>Some other text</p>
<p>Cash nbs $336,008</p>
"""

# Regular expression to find relevant sections inside <p> tags
pattern = r'<p>.*?\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*)?.*?</p>'

# Find all matches in the HTML content
matches = re.findall(pattern, html_content)

# Process and print results
for match in matches:
    cash_word = match[0]  # This is the matched "Cash"
    amount = match[1] if match[1] else "No amount found"  # This will be the matched amount or a fallback message
    print(f"Matched: '{cash_word}' with amount: '{amount}'")
