
from package import MODULE1, MODULE2, MODULE3

name = input('Please Enter your question: ').lower()
name2 = name.split()  # Split the input into individual words

# Create a list of modules to check
modules = [MODULE1, MODULE2, MODULE3]

# Check each module
for module in modules:
    module.handle_input(name2)
