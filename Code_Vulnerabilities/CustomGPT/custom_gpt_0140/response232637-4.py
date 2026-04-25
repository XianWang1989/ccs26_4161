
from package import MODULE1, MODULE2, MODULE3

name = input('Please Enter your question: ').lower()
name2 = name.split()  # Split input into words

# Check MODULE1
found, category = MODULE1.check_color(name2)
if found:
    print('You found a color!')
else:
    # Check MODULE2
    found, category = MODULE2.check_cars(name2)
    if found:
        print('You found a car!')
    else:
        # Check MODULE3
        found, category = MODULE3.check_food(name2)
        if found:
            print('You found a food!')
        else:
            print('No matches found in any module.')
