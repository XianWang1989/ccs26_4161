
x = 0
bool_value = False  # It's a good practice to avoid using 'bool' as a variable name

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print in Python 3
    if bool_value:
        print("Halleluhja")

bool_value = functionA(x)  # Get the boolean from functionA
functionB(bool_value)  # Pass it to functionB

print(x, bool_value)
