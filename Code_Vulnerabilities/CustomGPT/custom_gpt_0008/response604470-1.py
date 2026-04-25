
import re

text = '<p>Cash nbs $336,008</p>'

# Regex pattern to find "Cash" and optionally a number
pattern = r'<p>\s*(Cash.*?)\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?\s*</p>'

# Search for the pattern
match = re.search(pattern, text)

if match:
    cash_word = match.group(1)  # "Cash" and any following text
    amount = match.group(2)      # The number (if found)

    print(f'Cash Word: {cash_word.strip()}')
    if amount:
        print(f'Amount: ${amount}')
    else:
        print('Amount: Not found')
else:
    print('No match found')
