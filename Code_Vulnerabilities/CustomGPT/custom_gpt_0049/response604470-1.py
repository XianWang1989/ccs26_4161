
import re

# Sample input, which contains the <p> tags
text = "<p>Cash nbs $13,000</p>"

# First, let's extract the text between the <p> tags
p_content = re.search(r'<p>(.*?)<\/p>', text, re.DOTALL)  # Use re.DOTALL to make '.' include newlines
if p_content:
    inner_text = p_content.group(1)

    # Now we want to pull out "Cash" and the number if available
    result = re.search(r'Cash.*?(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)?', inner_text)
    if result:
        cash_word = "Cash"  # We know this is what we are searching for
        number = result.group(1) if result.group(1) else "No number found"
        print(f'Found word: {cash_word}')
        print(f'Found number: {number}')
    else:
        print("No match found.")

else:
    print("No <p> tag found.")
