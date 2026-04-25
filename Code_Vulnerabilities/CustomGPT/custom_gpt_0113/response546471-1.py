
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Get the boolean from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
