
from colorama import Fore, Style, init

# Initialize colorama
init()

# Print styled text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)
print(Style.BRIGHT + "This text is bigger (bright)!" + Style.RESET_ALL)
