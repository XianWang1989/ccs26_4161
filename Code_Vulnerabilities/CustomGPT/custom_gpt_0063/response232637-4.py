
# main.py
from package.MODULE1 import run_module1
from package.MODULE2 import run_module2
from package.MODULE3 import run_module3

name = input('Please enter your question: ').lower()

# Check each module in order
run_module1(name)
run_module2(name)
run_module3(name)
