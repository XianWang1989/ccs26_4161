
import re

# Sample HTML content
html_content = """
<p>Cash nbs $336,008 some other text</p>
<p>Other content</p>
<p>Cash has some stuff $13,000</p>
<p>Cash with nothing else</p>
"""

# Regex to find content within <p> tags
p_tag_content = re.findall(r'<p>(.*?)<\/p>', html_content, re.DOTALL)

# Process each found content to look for "Cash" and an optional number
results = []
for content in p_tag_content:
    match = re.search(r'\b(Cash)\b.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?', content)
    if match:
        cash_word = match.group(1)  # "Cash"
        cash_number = match.group(2) if match.group(2) else 'No number found'  # Optional number
        results.append((cash_word, cash_number))

# Output the results
for result in results:
    print(f'Found: {result[0]}, Number: {result[1]}')
