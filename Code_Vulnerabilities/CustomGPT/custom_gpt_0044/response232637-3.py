
from package import *

name = input('Please Enter your question: ').lower()

modules = [MODULE1, MODULE2, MODULE3, MODULE4]  # Add your modules here

for module in modules:
    # Call the run_module function in each module
    if module.run_module(name):
        break  # Exit the loop if a module successfully handled the input
