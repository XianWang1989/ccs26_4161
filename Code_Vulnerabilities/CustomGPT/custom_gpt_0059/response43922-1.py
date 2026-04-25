
from rich.console import Console

console = Console()

# Print blue text
console.print("This text is blue!", style="bold blue")

# Print bigger text (using a different approach)
console.print("This is larger text!", style="bold white on black", style="size=24")
