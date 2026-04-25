
from colorama import init, Fore
from rich.console import Console

# Initialize Colorama
init()

# Create an instance of Console from rich
console = Console()

# Print text in blue using colorama
print(Fore.BLUE + "This text is blue!" + Fore.RESET)

# Print styled text using rich
console.print("This text is bigger and bold!", style="bold magenta")
