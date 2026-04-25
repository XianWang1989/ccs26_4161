
# Import colorama for color manipulation
from colorama import init, Fore, Style

# Initialize colorama
init()

# Print blue colored text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)

# Print larger text (not possible directly in console, 
# but you can indicate larger text by repeated characters)
print(Fore.BLUE + "==== Larger Text ====" + Style.RESET_ALL)
