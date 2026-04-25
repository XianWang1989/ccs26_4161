
from rich.console import Console
from rich.text import Text

console = Console()

# Create a text object with specific styling
styled_text = Text("This text is big and blue!", style="bold blue")

# Print styled text
console.print(styled_text)
