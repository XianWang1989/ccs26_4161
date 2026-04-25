
x = 0
bool_value = False  # Renaming the variable from 'bool' to 'bool_value' to avoid shadowing the built-in `bool` type

def functionA(x):
    if x == 0:  # Use '==' for comparison, not 'is'
        return True
    return False

def functionB(bool_value):
    print(bool_value)  # Use parentheses to print in Python 3
    if bool_value:
        print("Halleluhja")

# Call functionA and capture its return value
bool_value = functionA(x)
# Pass the returned boolean value to functionB
functionB(bool_value)

print(x, bool_value)  # Outputs the values of x and bool_value
