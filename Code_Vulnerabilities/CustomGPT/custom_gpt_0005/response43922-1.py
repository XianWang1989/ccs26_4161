
def print_colored_text(text, color_code):
    """Prints text in a specified color."""
    print(f"\033[{color_code}m{text}\033[0m")

# Example usage
print_colored_text("This text is blue!", "34")  # 34 is the code for blue
