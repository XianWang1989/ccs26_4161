
from colorama import Fore, Style

# Initialize Colorama
import colorama
colorama.init()

# Print blue text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)
# Optionally, reset the style
print("This text is default.")
