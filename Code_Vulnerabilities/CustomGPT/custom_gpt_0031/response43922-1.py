
from rich.console import Console
from rich.text import Text

# Create a console object
console = Console()

# Create styled text
text = Text("Hello, World!", style="bold blue")

# Print the styled text
console.print(text)
