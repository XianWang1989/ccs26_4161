
from colorama import Fore, Style

# Initialize Colorama
import colorama
colorama.init()

# Example Text
text = "This text is blue!"
print(Fore.BLUE + text + Style.RESET_ALL)

# Reset to default
print("This text is back to normal.")
