
x = 0
boolean_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(boolean_value):
    print(boolean_value)
    if boolean_value:
        print("Hallelujah")

# Update the boolean based on the return value from functionA
boolean_value = functionA(x)
functionB(boolean_value)

print(x, boolean_value)
