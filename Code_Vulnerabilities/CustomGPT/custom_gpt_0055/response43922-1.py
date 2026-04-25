
from colorama import Fore, Style

# Initialize Colorama
colorama.init()

# Print colored text
print(Fore.BLUE + 'This text is blue!' + Style.RESET_ALL)
print('This is normal text.')

# To make text bold (depends on terminal support)
print(Style.BRIGHT + 'This is bold text.' + Style.RESET_ALL)
