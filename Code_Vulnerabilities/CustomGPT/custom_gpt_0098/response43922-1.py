
# Function to print colored text
def print_colored(text, color_code):
    # ANSI escape codes for text color
    print(f"\033[{color_code}m{text}\033[0m")

# Example usage
print_colored("Hello, World!", "34")  # Blue text
