
from rich.console import Console
from rich.text import Text

console = Console()

# Create colored text
text = Text("Hello, World!", style="blue bold")

# Print the formatted text
console.print(text)
