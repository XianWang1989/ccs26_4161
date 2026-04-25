
from package import *

name = input('Please Enter your question: ').lower()
name2 = name.split()  # Assuming the input will be split into words

# This function will check the length and direct to the appropriate module
def check_modules(name2):
    if len(name2) >= 3:
        MODULE1.process(name2)
    elif len(name2) >= 3:
        MODULE2.process(name2)
    elif len(name2) >= 3:
        MODULE3.process(name2)
    # continue as necessary for other modules...

check_modules(name2)
