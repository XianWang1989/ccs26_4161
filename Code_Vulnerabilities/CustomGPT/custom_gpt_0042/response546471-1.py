
x = 0
bool_value = False  # Use a different name to avoid shadowing built-in names

def functionA(x):
    if x == 0:
        return True  # Return True if x is 0
    return False  # Return False otherwise

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Get the boolean value from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
