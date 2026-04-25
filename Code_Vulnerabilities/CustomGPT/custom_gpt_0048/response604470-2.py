
import re

# Sample text with <p> tags
text = '<p>Cash nbs $336,008</p> <p>Total amount $45,000</p>'

# Regex pattern to extract "Cash" and the optional amount
pattern = r'<p>(?=.*Cash)(.*?)Cash(.*?)?(?P<amount>\$\d{1,3}(?:,\d{3})*)?</p>'

# Find matches
match = re.search(pattern, text)

if match:
    cash_found = "Cash"  # We're explicitly looking for "Cash"
    amount_found = match.group('amount')

    print(f'Found: {cash_found}')
    if amount_found:
        print(f'Amount: {amount_found}')
    else:
        print('No amount found.')
else:
    print('No match found.')
