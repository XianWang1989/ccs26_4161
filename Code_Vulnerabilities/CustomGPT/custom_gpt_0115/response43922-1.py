
from rich.console import Console
from rich.text import Text

console = Console()

# Create a text object with blue color
text = Text("Hello, World!", style="blue")

# Print the text
console.print(text)

# For larger text, you can use a different method
console.print("[bold magenta]This is a bigger message![/bold magenta]", style="bold")
