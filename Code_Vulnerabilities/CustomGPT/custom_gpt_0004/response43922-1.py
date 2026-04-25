
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Define the text
text = "Hello, this is blue text!"

# Print the text in blue and bold
print(Fore.BLUE + Style.BRIGHT + text)
