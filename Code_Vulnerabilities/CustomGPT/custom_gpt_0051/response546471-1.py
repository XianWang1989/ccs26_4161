
x = 0
bool_value = False  # Renamed variable to avoid confusion with built-in 'bool'

def functionA(x):
    if x == 0:
        return True  # Return True if x is 0
    return False  # Return False otherwise

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Update the boolean value by calling functionA and passing the value to functionB
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
