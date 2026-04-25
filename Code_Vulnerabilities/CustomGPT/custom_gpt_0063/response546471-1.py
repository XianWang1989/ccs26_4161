
x = 0
bool_value = False  # Avoid using 'bool' as a variable name

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print in Python 3
    if bool_value is True:
        print("Halleluhja")

# Get the boolean from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
