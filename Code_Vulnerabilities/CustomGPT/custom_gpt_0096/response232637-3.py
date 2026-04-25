
from package import MODULE1, MODULE2

name = input('Please Enter your question: ').lower()

# Call MODULE1 and check for its success
MODULE1.run_module(name)

# If MODULE1 doesn't handle the input, call MODULE2
if name not in ['what is my color', 'color']:
    MODULE2.run_module(name)
