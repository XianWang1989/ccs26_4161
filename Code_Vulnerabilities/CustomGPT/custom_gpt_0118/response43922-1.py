
from colorama import Fore, Style, init

# Initialize Colorama
init()

# Larger text representation (using ASCII art or similar)
def large_text(text):
    return '\n'.join([' '.join(line) for line in text])

text = "Hello, World!"
blue_text = Fore.BLUE + text + Style.RESET_ALL

print(blue_text)
print(large_text(["   H   ", "  e e  ", " l l l ", "  World!"]))
