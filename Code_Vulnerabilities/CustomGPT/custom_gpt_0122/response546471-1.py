
x = 0
bool_value = False  # Avoid using 'bool' as it's a built-in name

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Update the boolean based on functionA's result
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
