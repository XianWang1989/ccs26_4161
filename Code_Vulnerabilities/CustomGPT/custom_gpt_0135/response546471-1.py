
x = 0
bool_var = False  # Changed the variable name to avoid using 'bool'

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_var):
    print(bool_var)
    if bool_var:
        print("Halleluhja")

# Update the bool variable by calling functionA
bool_var = functionA(x)
functionB(bool_var)

print(x, bool_var)
