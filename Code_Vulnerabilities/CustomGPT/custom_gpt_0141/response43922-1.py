
# ANSI escape codes for text colors
class TextColor:
    BLUE = '\033[94m'  # Blue text
    RESET = '\033[0m'  # Reset to default

print(f"{TextColor.BLUE}This text is blue!{TextColor.RESET}")
