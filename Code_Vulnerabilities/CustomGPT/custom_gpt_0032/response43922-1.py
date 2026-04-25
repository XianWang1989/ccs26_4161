
from colorama import init, Fore, Style

# Initialize colorama
init()

# Print blue text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)

# Note: Terminal fonts can't be changed from within Python,
# but you can use ANSI escape codes for effects in some terminals.
