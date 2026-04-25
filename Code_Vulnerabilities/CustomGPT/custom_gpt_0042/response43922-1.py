
from rich.console import Console
from rich.text import Text

console = Console()

# Create a Text object with blue color and larger size
text = Text("This is blue and large text!", style="blue bold")
console.print(text)
