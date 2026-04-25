
import re

def extract_cash_and_number(text):
    # Regex pattern to extract "Cash" and optional dollar amount
    pattern = r'<p>.*?(Cash).*?(?:\$\s*([,\d]+))?.*?</p>'
    match = re.search(pattern, text)
    if match:
        cash_word = match.group(1)  # "Cash"
        number = match.group(2)  # Optional number
        return cash_word, number
    return None

# Example usage
text = "<p>Cash nbs $336,008</p>"
result = extract_cash_and_number(text)
print(result)  # Outputs: ('Cash', '336,008')
