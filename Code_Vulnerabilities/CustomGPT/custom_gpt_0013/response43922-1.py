
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Decorate text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)
print(Style.BRIGHT + "This text is bold!" + Style.RESET_ALL)
