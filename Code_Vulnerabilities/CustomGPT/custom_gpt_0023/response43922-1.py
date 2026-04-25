
from colorama import Fore, Style, init

# Initialize Colorama
init()

# Printing colored and styled text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)
print(Style.BRIGHT + "This text is bold and bright!" + Style.RESET_ALL)
print(Fore.GREEN + Style.UNDERLINE + "This text is green with underline!" + Style.RESET_ALL)
