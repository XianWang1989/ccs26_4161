
from rich.console import Console
from rich.text import Text

console = Console()

# Create a text object with specific color and size
text = Text("Hello, World!", style="bold blue")

# Print the decorated text
console.print(text)
