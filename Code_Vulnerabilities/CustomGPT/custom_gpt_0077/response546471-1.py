
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val is True:
        print("Halleluhja")

# Update the boolean value based on functionA
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)
