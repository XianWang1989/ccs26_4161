
from package import *

name = input('Please Enter your question: ').lower()
name2 = name.split()  # Assuming you want to check by words

modules = [MODULE1, MODULE2, MODULE3, MODULE4]  # List of modules to check

for module in modules:
    module.run_module(name2)  # Call the run_module function in each module
