
# Install the necessary libraries first
# pip install colorama rich

from colorama import Fore, Style
from rich.console import Console
from rich.text import Text

# Create a console object for rich text formatting
console = Console()

# Example of colored text using colorama
print(Fore.BLUE + "This text is blue!" + Style.RESET_ALL)

# Example of styled text using rich
text = Text("This text is big and bold!", style="bold blue")
console.print(text, style="bold blue", justify="center")
