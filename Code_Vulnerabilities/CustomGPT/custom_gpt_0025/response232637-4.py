
from package import *

# Main Execution
name = input('Please enter your question: ').lower()

# Check each module sequentially
found = False

# Check Module 1
result, message = MODULE1.check_color(name)
if result:
    print(message)
    found = True

# Check Module 2, only if not found in Module 1
if not found:
    result, message = MODULE2.check_cars(name)
    if result:
        print(message)
        found = True

# Check Module 3, only if not found in Module 2
if not found:
    result, message = MODULE3.check_foods(name)
    if result:
        print(message)
