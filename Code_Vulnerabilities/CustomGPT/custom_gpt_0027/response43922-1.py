
from rich.console import Console
from rich.text import Text

console = Console()

# Create a styled text
styled_text = Text("This is blue and bold text!", style="bold blue")

# Print the styled text
console.print(styled_text)
