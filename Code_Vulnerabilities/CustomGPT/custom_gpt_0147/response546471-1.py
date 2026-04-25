
x = 0

def functionA(x):
    # Returns the updated boolean state
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Capture the boolean value returned from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
