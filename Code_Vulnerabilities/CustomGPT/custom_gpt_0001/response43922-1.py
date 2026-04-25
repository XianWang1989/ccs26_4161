
from rich.console import Console
from rich.text import Text

console = Console()

# Create text that is blue and make it larger.
text = Text("Hello, World!", style="blue bold")
console.print(text)
