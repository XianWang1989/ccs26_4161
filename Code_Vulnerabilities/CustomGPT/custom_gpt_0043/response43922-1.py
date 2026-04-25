
from colorama import Fore, Style

# Initialize Colorama
colorama.init()

# Print styled text
print(Fore.BLUE + 'This text is blue!' + Style.RESET_ALL)
print(Style.BRIGHT + 'This is brighter text.' + Style.RESET_ALL)

# Don't forget to reset the style afterwards
