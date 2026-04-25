
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Print styled text
print(Fore.BLUE + "Hello, World!" + Style.RESET_ALL)

# Reset to default style
print("This text is normal.")
