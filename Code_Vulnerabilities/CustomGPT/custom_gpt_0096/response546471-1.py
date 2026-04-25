
x = 0
bool_value = False  # Rename to avoid shadowing the built-in bool type

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Update the boolean value using the return from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)
