
import re

# Sample input string
input_string = "<p>Cash nbs $336,008</p>"

# Regex pattern
pattern = r"<p>(.*?Cash.*?)(?:.*?(\$[\d,]+))?</p>"

# Perform the search
match = re.search(pattern, input_string)

if match:
    cash_info = match.group(1)  # This will be the text around "Cash"
    amount = match.group(2)      # This will be the dollar amount if present
    print(f"Extracted Info: {cash_info.strip()}")
    if amount:
        print(f"Amount: {amount.strip()}")
else:
    print("No match found.")
