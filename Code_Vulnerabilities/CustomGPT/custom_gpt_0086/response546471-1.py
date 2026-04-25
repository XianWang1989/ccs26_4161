
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Get the boolean value from functionA
bool_value = functionA(x)

# Pass the boolean value to functionB
functionB(bool_value)

print(x, bool_value)
