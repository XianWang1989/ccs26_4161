
x = 0
bool_value = False  # Changed variable name from bool to bool_value

def functionA(x):
    if x == 0:
        return True  # Return the boolean value

def functionB(bool_value):
    print(bool_value)  # Added parentheses for print function in Python 3
    if bool_value:
        print("Halleluhja")  # Correct print syntax for Python 3

# Get the boolean value from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
