
import re

# Example HTML string
html_content = """
<p>Cash nbs $13,000</p>
<p>Total revenue $336,008</p>
<p>Cash nbs $336,008</p>
<p>Some other text</p>
"""

# Regex to match content between <p> tags
p_content_regex = r'<p>(.*?)<\/p>'

# Finding all occurrences
matches = re.findall(p_content_regex, html_content)

# Extracting "Cash" and the number from each found match
for match in matches:
    # Regex to find "Cash" and the amount
    cash_regex = r'\b(Cash)\b.*?(\$[\d,]+)?'
    cash_match = re.search(cash_regex, match)

    if cash_match:
        cash_word = cash_match.group(1)  # 'Cash'
        cash_amount = cash_match.group(2)  # e.g. '$336,008' or None
        print(f'Found: "{cash_word}", Amount: "{cash_amount}"')
