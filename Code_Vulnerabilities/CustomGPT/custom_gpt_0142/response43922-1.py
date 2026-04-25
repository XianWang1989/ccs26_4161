
from rich.console import Console
from rich.text import Text

# Create a console instance
console = Console()

# Create a blue text with a larger font size
text = Text("Hello, World!", style="bold blue")

# Output the styled text
console.print(text)
