
x = 0
bool_var = False  # Changed variable name from 'bool' to 'bool_var' to avoid shadowing the built-in type 'bool'

def functionA(x):
    if x == 0:  # Use '==' for comparison
        return True
    return False  # Explicitly return False if condition is not met

def functionB(bool_var):
    print(bool_var)
    if bool_var:  # This implicitly checks for True
        print("Halleluhja")

# Call functionA and get the new value for bool_var
bool_var = functionA(x)
functionB(bool_var)

print(x, bool_var)
