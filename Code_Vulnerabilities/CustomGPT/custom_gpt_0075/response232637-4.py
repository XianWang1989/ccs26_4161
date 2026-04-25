
# main.py
from package import *

modules = [MODULE1, MODULE2, MODULE3]  # List your modules here

name = input('Please enter your question: ').lower()
for module in modules:
    if len(name) >= 3:
        module.handle_question(name)
