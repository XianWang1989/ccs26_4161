
from colorama import Fore, Style

# Initialize Colorama
colorama.init()

# Change text color to blue
print(Fore.BLUE + 'This text is blue!')

# Reset to default color
print(Style.RESET_ALL + 'This text is back to normal.')
