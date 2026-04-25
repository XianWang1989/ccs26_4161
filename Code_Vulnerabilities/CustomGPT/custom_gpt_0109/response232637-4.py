
from package import MODULE1, MODULE2, MODULE3, MODULE4

name = input('Please enter your question: ').lower()

# List of modules to iterate through
modules = [MODULE1, MODULE2, MODULE3, MODULE4]

# Flag to check if a module responded
found = False

for module in modules:
    module.run_game(name)
    # Break if some module processed the input
    if found:
        break
