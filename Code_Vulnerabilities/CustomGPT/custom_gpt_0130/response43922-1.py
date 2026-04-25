
from rich.console import Console

# Create a console object
console = Console()

# Print blue text of different sizes
console.print("This text is blue", style="bold blue")
console.print("This text is larger", style="bold blue", justify='center', number=50)
