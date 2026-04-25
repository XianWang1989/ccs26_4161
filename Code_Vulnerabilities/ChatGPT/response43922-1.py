
from rich.console import Console
from rich.text import Text

console = Console()

# Create text with specific color and size
text = Text("This is blue text!", style="bold blue")

# Printing the styled text
console.print(text)

# To resize the text is not possible with console but you can create some visual representation
# For example, a large text using repeating characters
large_text = "X" * 10
console.print(large_text, style="bold green")
