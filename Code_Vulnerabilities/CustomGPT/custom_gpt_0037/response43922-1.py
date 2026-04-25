
# Function to print blue text
def print_blue(text):
    BLUE = '\033[94m'  # ANSI escape code for blue
    RESET = '\033[0m'  # ANSI escape code to reset color
    print(f"{BLUE}{text}{RESET}")

print_blue("This text is blue!")
