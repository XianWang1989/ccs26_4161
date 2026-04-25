
# main.py
from package import MODULE1, MODULE2, MODULE3, MODULE4

name = input('Please enter your question: ').lower()

# Check each module one by one
if len(name) >= 3:
    MODULE1.run_module(name)
if len(name) >= 3:
    MODULE2.run_module(name)
if len(name) >= 3:
    MODULE3.run_module(name)
# Continue for more modules as needed
