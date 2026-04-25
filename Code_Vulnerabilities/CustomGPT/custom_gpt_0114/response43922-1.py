
from rich.console import Console
from rich.text import Text

console = Console()

# Creating styled text
text = Text("Hello, World!", style="blue bold")
console.print(text)
