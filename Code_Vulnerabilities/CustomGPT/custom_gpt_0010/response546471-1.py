
x = 0
bool_value = False  # Renamed to avoid conflict with the built-in `bool`

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Update bool_value based on the return value from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
