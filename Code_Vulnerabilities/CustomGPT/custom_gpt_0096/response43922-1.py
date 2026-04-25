
from colorama import Fore, Style, init

# Initialize Colorama
init()

# Print blue text
print(Fore.BLUE + "This is blue text!" + Style.RESET_ALL)

# Print larger text (note: font size is limited in terminal)
print(Fore.RESET + "Normal text size.")
