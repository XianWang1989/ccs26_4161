
from rich.console import Console
from rich.text import Text

console = Console()

# Create a larger text with blue color
text = Text("Hello, World!", style="blue bold")
console.print(text)
