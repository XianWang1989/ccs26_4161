
def print_colored_text(text):
    # ANSI escape codes
    blue = "\033[34m"  # Blue text
    reset = "\033[0m"  # Reset to default
    bigger_font = "\033[1m"  # Bold text to simulate bigger font

    # Print text
    print(f"{bigger_font}{blue}{text}{reset}")

# Usage
print_colored_text("This text is blue and bold!")
