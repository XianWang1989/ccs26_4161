
x = 0
bool_value = False  # Renamed to avoid shadowing built-in `bool`

def functionA(x):
    if x == 0:
        return True  # Return True if the condition is met
    return False  # Return False otherwise

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print in Python 3
    if bool_value is True:
        print("Halleluhja")

# Get the value from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
