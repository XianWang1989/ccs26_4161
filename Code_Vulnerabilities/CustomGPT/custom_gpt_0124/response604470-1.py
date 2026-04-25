
import re

text = '<p>Cash nbs $336,008</p>'
pattern = r'<p>\s*(Cash)\s.*?(\$\d{1,3}(?:,\d{3})*)?\s*</p>'

match = re.search(pattern, text)

if match:
    cash_word = match.group(1)  # "Cash"
    amount = match.group(2) if match.group(2) else None  # "$336,008" or None

    print("Found word:", cash_word)
    print("Found amount:", amount)
else:
    print("No match found.")
