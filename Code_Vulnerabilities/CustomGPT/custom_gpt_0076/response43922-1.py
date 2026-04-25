
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Print blue text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)

# Reset back to default color
print("This text is default color.")
