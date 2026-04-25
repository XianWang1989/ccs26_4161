
x = 0
bool_value = False  # Use a different name to avoid shadowing the built-in `bool`

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Get the boolean from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
