
# ANSI escape codes
BLUE = "\033[34m"  # Set color to blue
RESET = "\033[0m"  # Reset to default color

# Function to display text with color
def print_blue_text(text):
    print(f"{BLUE}{text}{RESET}")

# Usage
print_blue_text("This text is blue!")
