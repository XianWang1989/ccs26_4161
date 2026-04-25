
from rich.console import Console
from rich.text import Text

console = Console()

# Create a blue, bold text
text = Text("Hello, World!", style="bold blue")
console.print(text)

# Create a larger text
console.print("This is larger text.", style="bold red", justify="center")
