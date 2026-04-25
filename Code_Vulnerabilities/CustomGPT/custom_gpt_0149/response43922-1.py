
from rich.console import Console
from rich.text import Text

console = Console()

# Create a text object with blue color and increased size
text = Text("Hello, World!", style="bold blue")

# Print the styled text
console.print(text)
