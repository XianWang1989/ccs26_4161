
import re

# Sample HTML string
html_string = """
<p>Cash nbs $13,000</p>
<p>Other text</p>
<p>Cash some irrelevant text $336,008</p>
"""

# Regex to extract content inside <p> tags
pattern = r'<p>(.*?)<\/p>'

# Find all <p> contents
matches = re.findall(pattern, html_string)

# List to store results
results = []

# Process each match
for match in matches:
    # Regex to extract "Cash" and the optional number
    inner_pattern = r'(Cash).*?(\$\d{1,3}(?:,\d{3})*)?'
    inner_match = re.search(inner_pattern, match)
    if inner_match:
        cash_word = inner_match.group(1)
        number = inner_match.group(2) if inner_match.group(2) else None
        results.append((cash_word, number))

# Print the results
for result in results:
    print(f'Found: {result[0]} with number: {result[1]}')
