
x = 0
boolean_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool):
    print(bool)
    if bool:
        print("Hallelujah")

# Update boolean_value by calling functionA
boolean_value = functionA(x)
functionB(boolean_value)

print(x, boolean_value)
