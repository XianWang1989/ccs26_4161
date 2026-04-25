
from colorama import Fore, Style

# Initialize Colorama
colorama.init()

# Print blue text
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)

# ANSI escape codes to change the font size (note: this may not work in all environments)
print("\033[1mThis is a bold text!\033[0m")  # Bold text
print("\033[3mThis is an italic text!\033[0m")  # Italic text

# Remember to reset styles after
print(Style.RESET_ALL)
