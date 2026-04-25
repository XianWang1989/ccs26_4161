
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Print text in blue and bold
print(Fore.BLUE + Style.BRIGHT + "This text is blue and bold!" + Style.RESET_ALL)

# For larger text, just print multiple lines or use formatting
print(Fore.BLUE + "This text is larger (in a visual sense).")
print(Fore.BLUE + "This is how you can simulate larger text in terminal." + Style.RESET_ALL)

