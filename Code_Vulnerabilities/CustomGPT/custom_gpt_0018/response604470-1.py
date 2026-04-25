
import re

# Sample input HTML content
content = """
<p>Cash nbs $336,008</p>
<p>Total $500,000</p>
<p>Some other text</p>
<p>Cash nbs $13,000</p>
"""

# Regex pattern to match the content within <p> tags that includes "Cash" and an optional number
pattern = r'<p>(.*?\bCash\b.*?(\$[\d,]+)?)<\/p>'

# Find all matches
matches = re.findall(pattern, content)

# Extracted results
results = []
for match in matches:
    cash_word = match[0]
    number = match[1] if match[1] else "No number"
    results.append((cash_word, number))

# Display results
for cash_word, number in results:
    print(f"Found: {cash_word.strip()} - Number: {number}")
