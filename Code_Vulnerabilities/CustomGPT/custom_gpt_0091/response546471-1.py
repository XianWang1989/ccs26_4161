
x = 0
bool_val = False  # Avoid using 'bool' as a variable name since it's a built-in type

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)
