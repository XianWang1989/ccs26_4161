
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_var):
    print(bool_var)
    if bool_var:
        print("Halleluhja")

# Get boolean value from functionA
bool_var = functionA(x)
# Pass the boolean to functionB
functionB(bool_var)

print(x, bool_var)
