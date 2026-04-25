
# main.py
from package import *

name = input('Please enter your question: ').lower()
if len(name) >= 3:
    MODULE1.handle_question(name)  # Assume function is defined in MODULE1
    MODULE2.handle_question(name)  # Same for other modules
    MODULE3.handle_question(name)
