
from termcolor import colored
import pyfiglet

# Create a bigger text
big_text = pyfiglet.figlet_format("Hello, World!")

# Print it in blue
print(colored(big_text, 'blue'))
