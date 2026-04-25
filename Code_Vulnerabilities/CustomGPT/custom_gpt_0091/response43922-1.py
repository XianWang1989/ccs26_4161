
from rich.console import Console
from rich.text import Text

# Create a console object
console = Console()

# Create a text object with specific color and style
text = Text("Hello, World!", style="bold blue on white")

# Print the styled text
console.print(text)
