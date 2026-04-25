
# First, install colorama using: pip install colorama

from colorama import Fore, Style

# Initialize colorama
import colorama
colorama.init(autoreset=True)

# Example of styled output
print(Fore.BLUE + 'This text is blue!')
print(Style.BRIGHT + 'This text is bright and bigger in some terminals!')
