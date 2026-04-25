
from package import *

name = input('Please Enter your question: ').lower()
name2 = name.split()  # Split input into words

# Check each module until one returns True
if MODULE1.check_colors(name2):
    print('You are interested in colors.')
elif MODULE2.check_cars(name2):
    print('You are interested in cars.')
# ... add additional checks for MODULE3, MODULE4, etc.
else:
    print('No matches found in any module.')
