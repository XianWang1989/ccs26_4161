
from colorama import init, Fore, Style

# Initialize Colorama
init()

# Print blue text
print(Fore.BLUE + 'This text is blue!' + Style.RESET_ALL)

# Print bigger text (console doesn't support literal resizing)
print(Fore.BLUE + 'This text is big!' * 2 + Style.RESET_ALL)  # Just a simple repeat to show emphasis
