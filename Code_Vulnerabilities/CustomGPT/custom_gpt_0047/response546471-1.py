
x = 0
boolean_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Get the boolean value from functionA
boolean_value = functionA(x)

# Pass the boolean value to functionB
functionB(boolean_value)

print(x, boolean_value)
