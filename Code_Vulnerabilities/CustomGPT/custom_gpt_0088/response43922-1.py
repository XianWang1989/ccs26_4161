
from rich.console import Console
from rich.text import Text

console = Console()
text = Text("This is blue and large text!", style="bold blue")
console.print(text)
