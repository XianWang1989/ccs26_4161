
# ANSI escape codes for coloring text
BLUE = '\033[94m'  # Blue text
RESET = '\033[0m'  # Reset to default color

# Example function to print blue text
def print_blue(text):
    print(f"{BLUE}{text}{RESET}")

print_blue("This is some blue text!")
