
x = 0
bool_value = False  # Changed variable name to avoid shadowing built-in `bool`

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Call functionA and get the returned boolean value
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
