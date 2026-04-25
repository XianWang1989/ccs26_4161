
from package import MODULE1, MODULE2

name = input('Please Enter your question: ').lower()

# Check each module
if len(name) >= 3:
    MODULE1.game(name)
    MODULE2.game(name)
