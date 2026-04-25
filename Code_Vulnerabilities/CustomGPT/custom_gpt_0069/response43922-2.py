
from rich.console import Console
from rich.text import Text

console = Console()

# Create styled text
text = Text("This text is blue and bold!")
text.stylize("bold blue")

console.print(text)
