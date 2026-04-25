
x = 0
bool_var = False  # Avoid using 'bool' as a variable name, it's a built-in type.

def functionA(x):
    if x == 0:
        return True  # Return the boolean value instead of modifying the parameter.

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Call functionA and update the boolean value from its return.
bool_var = functionA(x)
functionB(bool_var)

print(x, bool_var)
