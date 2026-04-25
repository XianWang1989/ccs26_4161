
from rich.console import Console
from rich.text import Text

console = Console()

# Create a Text object with blue color and larger size
text = Text("Hello, World!", style="blue bold")

# Print the decorated text
console.print(text)
