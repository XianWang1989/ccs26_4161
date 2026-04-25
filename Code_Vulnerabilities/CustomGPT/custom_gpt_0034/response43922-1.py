
from rich.console import Console
from rich.text import Text

# Create a console object
console = Console()

# Create a Text object with styling
styled_text = Text("Hello, World!", style="blue bold italic")

# Print the styled text
console.print(styled_text)
