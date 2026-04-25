
import re

text = '<p>Cash nbs $336,008</p>'
pattern = r'<p>\s*(Cash.*?)?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?\s*</p>'

match = re.search(pattern, text)
if match:
    cash = match.group(1)  # "Cash" or None
    amount = match.group(2)  # "$336,008" or None
    print(f'Extracted: "{cash}", Amount: "{amount}"')
