
x = 0
bool_value = False  # Changed variable name to avoid conflict with the built-in bool

def functionA(x, bool_value):
    if x == 0:
        bool_value = True
    return bool_value  # Return the updated value

def functionB(bool_value):
    print(bool_value)  # Added parentheses for print function in Python 3
    if bool_value is True:
        print("Halleluhja")

# Update bool_value based on functionA's result
bool_value = functionA(x, bool_value)
functionB(bool_value)

print(x, bool_value)
