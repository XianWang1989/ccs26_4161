
# Function to print blue text
def print_blue(text):
    blue = '\033[94m'  # ANSI code for blue text
    reset = '\033[0m'  # ANSI code to reset to default
    print(f"{blue}{text}{reset}")

# Example usage
print_blue("This text is blue!")
