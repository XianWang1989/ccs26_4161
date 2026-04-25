
# Function to print text in a specific color
def print_in_blue(text):
    BLUE = '\033[94m'  # ANSI escape code for blue text
    RESET = '\033[0m'  # ANSI escape code to reset to default color
    print(f"{BLUE}{text}{RESET}")

# Example usage
print_in_blue("This text will be printed in blue!")
