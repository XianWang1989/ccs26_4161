
x = 0
bool_var = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_var):
    print(bool_var)
    if bool_var is True:
        print("Halleluhja")

# Get the boolean value from functionA
bool_var = functionA(x)
functionB(bool_var)

print(x, bool_var)
