
# main.py
from package import *

name = input('Please Enter your question: ').lower()

def check_modules(question):
    if MODULE1.process_question(question):
        return
    if MODULE2.process_question(question):
        return
    if MODULE3.process_question(question):
        return
    # Add checks for other modules similarly...

check_modules(name)
