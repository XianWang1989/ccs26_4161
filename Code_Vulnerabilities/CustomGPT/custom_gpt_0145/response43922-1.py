
# ANSI escape codes for color and text formatting
BLUE = "\033[34m"       # Blue text
RESET = "\033[0m"       # Reset to default color

# To increase text size, it's terminal dependent. This is just a representation.
# In actual applications, you might need libraries like rich or colorama.

text = "This is a blue text!"

# Print the colored text
print(f"{BLUE}{text}{RESET}")
