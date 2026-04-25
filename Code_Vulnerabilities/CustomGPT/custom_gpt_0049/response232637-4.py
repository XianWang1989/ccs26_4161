
from package import *

name = input('Please Enter your question: ').lower()
name2 = name.split()

# Check each module in the order you need
if any(item in name2 for item in ['what is my color', 'color']):
    MODULE1.run_module1(name2)
elif any(item in name2 for item in ['cars']):
    MODULE2.run_module2(name2)
elif any(item in name2 for item in ['toys']):
    MODULE3.run_module3(name2)
# Add additional checks for other modules as necessary
