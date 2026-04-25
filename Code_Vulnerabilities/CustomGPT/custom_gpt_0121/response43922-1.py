
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

# Define a function to print styled text
def print_styled_text(text, size='medium'):
    size_mapping = {
        'small': '\x1b[2m',   # Dim
        'medium': '\x1b[1m',  # Bold
        'large': '\x1b[3m',   # Italics
    }

    # Choose size style
    size_style = size_mapping.get(size, '\x1b[1m')  # Default to bold

    # Print text in blue with the selected size
    print(f"{size_style}{Fore.BLUE}{text}{Style.RESET_ALL}")

# Example usage
print_styled_text("Hello, this text is blue and bold!", size='medium')
