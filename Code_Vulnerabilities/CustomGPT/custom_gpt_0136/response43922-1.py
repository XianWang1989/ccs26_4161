
# Install colorama if you haven't already
# pip install colorama

from colorama import Fore, Style

# Colorizing text in the terminal
print(Fore.BLUE + 'This text is blue!' + Style.RESET_ALL)

# For HTML text decoration
html_text = '<p style="color: blue; font-size: 20px;">This text is blue and bigger!</p>'
print(html_text)
